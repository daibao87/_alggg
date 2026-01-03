本文件記錄了最小編輯距離演算法的實作與測試結果。該演算法用於計算將字串 `b` 轉換為字串 `a` 所需的最少操作次數（插入、刪除、取代）。

## 1. 測試環境與輸入數據

- **演算法核心**: 動態規劃 (Dynamic Programming)
- **語言**: Python 3
- **測試字串 A**: `ATGCAATCCC`
- **測試字串 B**: `ATG  ATCCG` (注意：包含空白字元)
  ai對話:https://chatgpt.com/share/695932fc-a3f8-8009-b86a-4cf3e6e83d79
