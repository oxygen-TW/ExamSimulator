# run-table-exam-practice-tool
跑台考試的練習程式

**圖片顯示程式修改自 https://gist.github.com/nakagami/3764702**

<br/>

## Dependence
```toml
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]

[packages]
Pillow = "*"
PyInstaller = "*"
toml = "*"

[requires]
python_version = "3.7"

```
---

## 題目包製作方法

1. 建立一個資料夾
2. 在資料夾中新增`config.toml`
3. 將圖片以`1.jpg, 2.jpg....10.jpg`的命名放入資料夾 **注意! 圖片高度不要超過1000 px**
4. 複製以下模板到 `config.toml`

```toml
title = "此題目包的名稱"

[answer]
1 = "D01 10x Ascaris lumbricoides的三片口唇"
2 = "D02 10x Ascaris lumbricoides的2根spicules"
3 = "D2-1 10x Ascaris lumbricoides larva(中間八字型)"
4 = "D03 40x Strongyloides stercoralis F-form larva"
5 = "D04 40x Ancylostoma duodenale F-form larva"
6 = "D05 40x Necator americanus F-form larva"
7 = "D06 10x Eggs of Trichostrongylus orientalis"
```

5. 修改題目包名稱，並依照照片的檔名數字填入正確答案
6. 資料夾現在應該長這樣
![folder](https://i.imgur.com/QIZX1uC.png)

<br/>

7. 將該資料夾加入壓縮檔，以`zip`方式壓縮
![zip](https://i.imgur.com/2OCifbO.png)

8. 完成！

---
2020/05/12 劉子豪