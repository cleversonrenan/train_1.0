param([string]$InDir = "_pages", [string]$OutFile = "_ocr_cartas.txt")

Add-Type -AssemblyName System.Runtime.WindowsRuntime

$asTaskGeneric = ([System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
    $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1'
})[0]

function Await($WinRtTask, $ResultType) {
    $asTask = $asTaskGeneric.MakeGenericMethod($ResultType)
    $netTask = $asTask.Invoke($null, @($WinRtTask))
    $netTask.Wait(-1) | Out-Null
    $netTask.Result
}

[void][Windows.Storage.StorageFile,Windows.Foundation,ContentType=WindowsRuntime]
[void][Windows.Graphics.Imaging.BitmapDecoder,Windows.Foundation,ContentType=WindowsRuntime]
[void][Windows.Media.Ocr.OcrEngine,Windows.Foundation,ContentType=WindowsRuntime]
[void][Windows.Globalization.Language,Windows.Foundation,ContentType=WindowsRuntime]

$lang = New-Object Windows.Globalization.Language "pt-BR"
$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage($lang)
if (-not $engine) { throw "no ocr engine" }

$sb = New-Object System.Text.StringBuilder
$files = Get-ChildItem -Path $InDir -Filter *.png | Sort-Object Name
foreach ($f in $files) {
    $path = $f.FullName
    $sf = Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync($path)) ([Windows.Storage.StorageFile])
    $stream = Await ($sf.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
    $decoder = Await ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
    $bitmap = Await ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
    $result = Await ($engine.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])
    [void]$sb.AppendLine("===== $($f.Name) =====")
    foreach ($line in $result.Lines) { [void]$sb.AppendLine($line.Text) }
    $stream.Dispose()
}
[System.IO.File]::WriteAllText((Join-Path (Get-Location) $OutFile), $sb.ToString(), [System.Text.Encoding]::UTF8)
"OK: $($files.Count) files -> $OutFile"
