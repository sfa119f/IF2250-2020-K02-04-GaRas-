import pymysql
from ModulFungsi.tes import *

def test_hitungHarga():
    harga = HitungHarga("tongkat lipat",1,"jne",0.8)
    assert harga == 38000

def test_membeli():
    total = Membeli("alat tulis tunanetra",1,"katara","sicepat")
    assert total == 13600

def test_searchProduk():
    result = [(1, 'tongkat lipat', 30000, 99, 0.8, 'tongkat untuk tuna netra dan bisa dilipat', 'Foto/produk/tongkat.png', 'tuna netra'), (9, 'translator', 1000000, 10, 0.4, 'alat penerjemah bahasa isyarat', 'Foto/produk/translator.jpg', 'tuna wicara')]
    search = SearchProduk("t")
    assert result == search
    
def test_searchKategori():
    result = [(14, 'alat peraga', 105000, 35, 0.3, 'alat peraga untuk tuna grahita', 'Foto/produk/alatperaga.jpg', 'tuna grahita')]
    search = SearchKategori("tuna grahita")
    assert result == search

def test_allKurir():
    result = [(1, 'jne', 10000, 'Jalan A No.5 Bandung', 'Foto/kurir/jne.png'), (2, 'jnt', 9500, 'Jalan B No.4 Bandung', 'Foto/kurir/jnt.png'), (3, 'tiki', 11000, 'Jalan C No.3 Bandung', 'Foto/kurir/tiki.png'), (4, 'sicepat', 12000, 'Jalan D No.6 Bandung', 'Foto/kurir/sicepat.png')]
    kurir = AllKurir()
    assert result == kurir

def test_allproduk():
    result = [(1, 'tongkat lipat', 30000, 99, 0.8, 'tongkat untuk tuna netra dan bisa dilipat', 'Foto/produk/tongkat.png', 'tuna netra'), (2, 'alquran braille', 200000, 30, 0.5, 'alquran braille untuk tuna netra', 'Foto/produk/alquran.png', 'tuna netra'), (3, 'kacamata hitam', 150000, 50, 0.2, 'kacamata hitam untuk tuna netra', 'Foto/produk/kacamata.png', 'tuna netra'), (4, 'alat tulis tunanetra', 10000, 129, 0.3, 'alat tulis tunanetra untuk tuna netra', 'Foto/produk/alattulis.png', 'tuna netra'), (5, 'alat bantu belajar tunanetra', 50000, 10, 0.2, 'media belajar matematika', 'Foto/produk/alatbelajar.jpg', 'tuna netra'), (6, 'alat bantu dengar', 70000, 25, 0.1, 'alat bantu pendengaran', 'Foto/produk/alatdengar.png', 'tuna rungu'), (7, 'masker transparan', 15000, 80, 0.05, 'masker transparan untuk tuna rungu', 'Foto/produk/masker.jpg', 'tuna rungu'), (8, 'buku bahasa isyarat', 35000, 250, 0.5, 'buku untuk belajar bahasa isyarat', 'Foto/produk/buku.jpg', 'tuna wicara'), (9, 'translator', 1000000, 10, 0.4, 'alat penerjemah bahasa isyarat', 'Foto/produk/translator.jpg', 'tuna wicara'), (10, 'kursi roda', 350000, 59, 5.0, 'kursi roda untuk tuna daksa', 'Foto/produk/kursiroda.png', 'tuna daksa'), (11, 'kaki palsu', 75000, 70, 2.0, 'alat bantu jalan', 'Foto/produk/kakipalsu.png', 'tuna daksa'), (12, 'orthotic', 95000, 45, 0.4, 'alat bantu untuk tuna daksa', 'Foto/produk/orthotic.png', 'tuna daksa'), (13, 'splint', 105000, 35, 0.4, 'alat bantu untuk tuna daksa', 'Foto/produk/splint.png', 'tuna daksa'), (14, 'alat peraga', 105000, 35, 0.3, 'alat peraga untuk tuna grahita', 'Foto/produk/alatperaga.jpg', 'tuna grahita')]
    produk = AllProduk()
    assert result == produk

def test_menjual():
    result = [(1, 'tongkat lipat', 30000, 99, 0.8, 'tongkat untuk tuna netra dan bisa dilipat', 'Foto/produk/tongkat.png', 'tuna netra'), (2, 'alquran braille', 200000, 30, 0.5, 'alquran braille untuk tuna netra', 'Foto/produk/alquran.png', 'tuna netra'), (3, 'kacamata hitam', 150000, 50, 0.2, 'kacamata hitam untuk tuna netra', 'Foto/produk/kacamata.png', 'tuna netra'), (4, 'alat tulis tunanetra', 10000, 129, 0.3, 'alat tulis tunanetra untuk tuna netra', 'Foto/produk/alattulis.png', 'tuna netra'), (5, 'alat bantu belajar tunanetra', 50000, 10, 0.2, 'media belajar matematika', 'Foto/produk/alatbelajar.jpg', 'tuna netra'), (6, 'alat bantu dengar', 70000, 25, 0.1, 'alat bantu pendengaran', 'Foto/produk/alatdengar.png', 'tuna rungu'), (7, 'masker transparan', 15000, 80, 0.05, 'masker transparan untuk tuna rungu', 'Foto/produk/masker.jpg', 'tuna rungu'), (8, 'buku bahasa isyarat', 35000, 250, 0.5, 'buku untuk belajar bahasa isyarat', 'Foto/produk/buku.jpg', 'tuna wicara'), (9, 'translator', 1000000, 10, 0.4, 'alat penerjemah bahasa isyarat', 'Foto/produk/translator.jpg', 'tuna wicara'), (10, 'kursi roda', 350000, 59, 5.0, 'kursi roda untuk tuna daksa', 'Foto/produk/kursiroda.png', 'tuna daksa'), (11, 'kaki palsu', 75000, 70, 2.0, 'alat bantu jalan', 'Foto/produk/kakipalsu.png', 'tuna daksa'), (12, 'orthotic', 95000, 45, 0.4, 'alat bantu untuk tuna daksa', 'Foto/produk/orthotic.png', 'tuna daksa'), (13, 'splint', 105000, 35, 0.4, 'alat bantu untuk tuna daksa', 'Foto/produk/splint.png', 'tuna daksa'), (14, 'alat peraga', 105000, 35, 0.3, 'alat peraga untuk tuna grahita', 'Foto/produk/alatperaga.jpg', 'tuna grahita')]
    dijual = AllJual("sokka")
    assert result == dijual
