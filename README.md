# Chi-Ching Lee's Lab

這個 repository 是舊網站的靜態搬移版本，保留原本 Bootstrap 版型、導覽、編排與頁面結構，只把 PHP 頁面轉成 GitHub Pages 可提供的 HTML，並修正站內連結。

## 網站入口

- [原網站入口頁](index.html)（原本的 `http://biobug.cgu.edu.tw/`）
- [Chi-Ching Lee's Lab](labWebsite/index.html)（原本的 `/labWebsite/`）
- [大數據分析積木微學程](bigDataMicrocourse/index.html)（原本的 `/bigDataMicrocourse/`）
- [TA application information](TAcsie/form.html) (original `/TAcsie/form.php`; static information page only)

GitHub Pages 網址：<https://ccllabe.github.io/lab/>

## 已搬移內容

- 實驗室首頁、成員、校友、實驗室生活
- 工程數學、大數據應用、資料庫設計、深度學習與 Python、雲端系統等課程頁面
- 課程頁面使用的 PDF、PPT/PPTX、DOC/DOCX、CSV、Python、Notebook、圖片與壓縮檔
- 大數據微學程申請文件、課群架構圖與 Bootstrap 資產
- 舊站導覽中的站內 PHP 連結已改成對應的 `.html` 頁面

GitHub 單一檔案上限為 100 MB，因此三個超大型教材檔（`VOCdevkit.zip`、`unet_carvana_scale0.5_epoch2.pth`、`YearPredictionMSD.csv`）沒有放入 repository；其餘教材均已下載到原本的相對路徑。這三個檔案原本位於課程頁面的註解教材連結中。

## GitHub Pages 設定

Pages 已設定為 `main` 分支的根目錄，網站不需要建置工具，直接提供 HTML、CSS、JavaScript 與課程資產。
