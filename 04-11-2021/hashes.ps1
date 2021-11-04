Get-FileHash ".\Encriptado\*", ".\*",".\Librerias\*",".\Data\*",".\bas\*", ".\llaves\*"  -Algorithm SHA512 | Format-List | Out-File -FilePath ".\hashes\hashes512.txt"
