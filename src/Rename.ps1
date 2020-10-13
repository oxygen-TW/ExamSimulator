Get-ChildItem *.jpg | ForEach-Object -Begin {
  $count = 407
} -Process {
  Rename-Item $_ -NewName "$count.jpg"
  $count++
}