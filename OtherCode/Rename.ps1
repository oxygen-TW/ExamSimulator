Get-ChildItem *.jpg | ForEach-Object -Begin {
  $count = 1
} -Process {
  Rename-Item $_ -NewName "$count.jpg"
  $count++
}