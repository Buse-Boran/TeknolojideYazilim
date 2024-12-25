from main import sayilari_topla
import sys

if sayilari_topla([1, 2, 3]) != 6:
    sys.exit("sayilari_topla([1, 2, 3]) değeri 6'ya eşit değil.")

if sayilari_topla([1, 2, 3, 4, 5]) != 15:
    sys.exit("sayilari_topla([1, 2, 3, 4, 5]) değeri 15'e eşit değil.")

print("Testler başarıyla geçildi.")
