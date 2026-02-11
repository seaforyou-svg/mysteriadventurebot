# ==========================================
# MYSTERY ADVENTURE BOT
# Game Petualangan Interaktif Berbasis Teks
# ==========================================

import time
import random

# ==========================================
# FUNGSI UTILITAS untuk EFEK DRAMATIS
# ==========================================

def print_delay(teks, delay=0.05):
    """
    Menampilkan teks dengan efek dramatis.
    Setiap karakter muncul dengan jeda 0.05 detik (20 char/detik).
    
    Args:
        teks: string yang akan ditampilkan
        delay: jeda dalam detik antar karakter (default: 0.05)
    """
    for karakter in teks:
        print(karakter, end='', flush=True)
        time.sleep(delay)
    print()  # Baris baru di akhir


def tampilkan_ascii_pedang():
    """Menampilkan ASCII art pedang saat pemain menang pertempuran"""
    pedang = """
        |
        |
    <--|-->
        |
       / \\
    """
    print(pedang)


def tampilkan_ascii_tengkorak():
    """Menampilkan ASCII art tengkorak saat pemain kalah"""
    tengkorak = """
       ~~~~~
      ( O O )
       \\ ~ /
        | | |
       /| | |\\
    """
    print(tengkorak)


def pertempuran_melawan_musuh(nama, nyawa):
    """
    Simulasi pertempuran dengan musuh menggunakan random.
    
    Args:
        nama: nama pemain
        nyawa: nyawa pemain saat ini
        
    Returns:
        tuple (kemenangan: bool, nyawa_sisa: int)
    """
    print("\n" + "=" * 50)
    print_delay("⚔️  PERTEMPURAN DIMULAI! ⚔️")
    print("=" * 50)
    time.sleep(0.5)
    
    print_delay(f"\n{nama} menghadapi musuh yang berbahaya!")
    time.sleep(0.5)
    
    # Simulasi pertempuran dengan random
    print_delay("\nMusuh menyerang!")
    time.sleep(1)
    
    # Random untuk menentukan hasil (50% menang, 50% kalah)
    hasil_pertempuran = random.choice([True, False])
    
    if hasil_pertempuran:
        # MENANG
        print_delay("\n✨ Serangan Anda tepat sasaran! ✨")
        time.sleep(0.5)
        print_delay("Musuh terjatuh...")
        time.sleep(0.5)
        print("\n" + "=" * 50)
        print_delay("🎉 ANDA MEMENANGKAN PERTEMPURAN! 🎉")
        print("=" * 50)
        tampilkan_ascii_pedang()
        print_delay("\nAnda berhasil mengalahkan musuh dengan pedang yang bersinar!")
        return True, nyawa
    else:
        # KALAH
        print_delay("\n💥 Musuh berhasil menyerang Anda! 💥")
        time.sleep(0.5)
        nyawa -= 30  # Kurangi nyawa lebih banyak karena pertempuran
        if nyawa <= 0:
            nyawa = 0
        print_delay(f"Nyawa berkurang 30! Sisa nyawa: {nyawa}")
        time.sleep(0.5)
        print("\n" + "=" * 50)
        print_delay("☠️  ANDA KALAH DALAM PERTEMPURAN! ☠️")
        print("=" * 50)
        tampilkan_ascii_tengkorak()
        print_delay("\nAnda terpukul mundur dan luka parah...")
        return False, nyawa


def tampilkan_judul():
    """Menampilkan judul game"""
    print("=" * 50)
    print_delay("  🎮 MYSTERY ADVENTURE BOT 🎮")
    print("=" * 50)
    print_delay("Selamat datang di petualangan misterius!")
    print()


def ambil_nama_pemain():
    """Mengambil nama pemain dari input"""
    nama = input("Masukkan nama Anda: ").strip()
    
    # Validasi input
    while not nama:
        print_delay("❌ Nama tidak boleh kosong!")
        nama = input("Masukkan nama Anda: ").strip()
    
    return nama


def tampilkan_intro(nama, nyawa):
    """Menampilkan cerita pembuka"""
    print_delay(f"\n✨ Selamat datang, {nama}! ✨")
    print_delay(f"❤️  Nyawa: {nyawa}")
    print_delay("\nAnda bangun di tengah hutan misterius.")
    print_delay("Ada dua jalan di depan Anda...")
    print_delay("\n1️⃣  LEMBAH CODING - Jalan yang cerah dan penuh tanda")
    print_delay("2️⃣  GUNUNG BUG - Jalan yang gelap dan berbahaya")
    print()


def pilihan_awal(nama, nyawa):
    """Pemain memilih jalan pertama"""
    while True:
        try:
            pilihan = input("Pilih jalan (1 atau 2): ").strip()
            
            if pilihan == "1":
                return lembah_coding(nama, nyawa)
            elif pilihan == "2":
                return gunung_bug(nama, nyawa)
            else:
                print_delay("❌ Pilihan tidak valid! Pilih 1 atau 2.")
        except (ValueError, KeyboardInterrupt):
            print_delay("❌ Input tidak valid! Silakan masukkan 1 atau 2.")


def lembah_coding(nama, nyawa):
    """Path 1: Lembah Coding - Jalan yang relatif aman"""
    print("\n" + "=" * 50)
    print_delay("🌿 LEMBAH CODING 🌿")
    print("=" * 50)
    print_delay(f"\n{nama} memilih jalan Lembah Coding...")
    print_delay(f"❤️  Nyawa: {nyawa}")
    print_delay("\nAnda memasuki lembah yang indah.")
    print_delay("Di depan ada seorang Programmer tua yang terlihat bijak.")
    print_delay("Dia menawarkan dua pilihan:")
    print_delay("\n1️⃣  Dengarkan pelajaran tentang variabel")
    print_delay("2️⃣  Abaikan dan langsung ambil harta yang terlihat")
    print()
    
    while True:
        try:
            pilihan = input("Apa pilihan Anda (1 atau 2): ").strip()
            
            if pilihan == "1":
                return tahap_lanjut_lembah_1(nama, nyawa)
            elif pilihan == "2":
                nyawa -= 20
                if nyawa <= 0:
                    return game_over_habis_nyawa(nama)
                print_delay(f"\n❌ Pilihan salah! Nyawa berkurang 20.")
                print_delay(f"❤️  Sisa Nyawa: {nyawa}")
                print("\n" + "=" * 50)
                return game_over_negatif(nama, "Harta itu adalah perangkap!", nyawa)
            else:
                print_delay("❌ Pilihan tidak valid!")
        except (ValueError, KeyboardInterrupt):
            print_delay("❌ Input tidak valid! Silakan masukkan 1 atau 2.")


def tahap_lanjut_lembah_1(nama, nyawa):
    """Tahap lanjut path Lembah Coding - Pilihan pertama benar"""
    print("\n" + "=" * 50)
    print_delay("⭐ TAHAP BERIKUTNYA ⭐")
    print("=" * 50)
    print_delay(f"\n✅ {nama} memilih untuk belajar!")
    print_delay(f"❤️  Nyawa: {nyawa}")
    print_delay("\nProgrammer tua tersenyum dan berbagi ilmu tentang variabel.")
    print_delay("Dengan pengetahuan baru, Anda dapat mengatur kodenya dengan benar.")
    print_delay("\nSekarang Anda menghadapi tantangan debugging:")
    print_delay("Ada sebuah program dengan bug. Apa yang Anda lakukan?")
    print_delay("\n1️⃣  Analisis kode dengan cermat dan temukan bugnya")
    print_delay("2️⃣  Hapus semua kode dan tulis ulang dari awal")
    print()
    
    while True:
        try:
            pilihan = input("Pilihan Anda (1 atau 2): ").strip()
            
            if pilihan == "1":
                return game_over_positif(nama, "Lembah Coding", nyawa)
            elif pilihan == "2":
                nyawa -= 20
                if nyawa <= 0:
                    return game_over_habis_nyawa(nama)
                print_delay(f"\n❌ Pilihan salah! Nyawa berkurang 20.")
                print_delay(f"❤️  Sisa Nyawa: {nyawa}")
                print("\n" + "=" * 50)
                return game_over_negatif(nama, "Kode yang bagus hilang!", nyawa)
            else:
                print_delay("❌ Pilihan tidak valid!")
        except (ValueError, KeyboardInterrupt):
            print_delay("❌ Input tidak valid! Silakan masukkan 1 atau 2.")


def gunung_bug(nama, nyawa):
    """Path 2: Gunung Bug - Jalan yang penuh bahaya"""
    print("\n" + "=" * 50)
    print_delay("⛰️  GUNUNG BUG ⛰️")
    print("=" * 50)
    print_delay(f"\n{nama} memilih jalan Gunung Bug...")
    print_delay(f"❤️  Nyawa: {nyawa}")
    print_delay("\nDi jalan yang gelap, Anda melihat tiga pintu aneh.")
    print_delay("Setiap pintu membuat suara yang berbeda.")
    print_delay("\n🔴 Pintu Merah - Mengeluarkan asap tebal")
    print_delay("🟡 Pintu Kuning - Berkilau dengan cahaya")
    print_delay("🟢 Pintu Hijau - Terlihat biasa-biasa saja")
    print()
    
    while True:
        try:
            pilihan = input("Pintu mana yang Anda pilih (Merah/Kuning/Hijau): ").strip().lower()
            
            if pilihan == "merah":
                nyawa -= 20
                if nyawa <= 0:
                    return game_over_habis_nyawa(nama)
                print_delay(f"\n❌ Pilihan salah! Nyawa berkurang 20.")
                print_delay(f"❤️  Sisa Nyawa: {nyawa}")
                print("\n" + "=" * 50)
                return game_over_negatif(nama, "Asap beracun membuat Anda kehilangan kesadaran!", nyawa)
            elif pilihan == "kuning":
                return tahap_lanjut_gunung_1(nama, nyawa)
            elif pilihan == "hijau":
                nyawa -= 20
                if nyawa <= 0:
                    return game_over_habis_nyawa(nama)
                print_delay(f"\n❌ Pilihan salah! Nyawa berkurang 20.")
                print_delay(f"❤️  Sisa Nyawa: {nyawa}")
                print("\n" + "=" * 50)
                return game_over_negatif(nama, "Pintu itu jebakan! Lantai runtuh!", nyawa)
            else:
                print_delay("❌ Pilihan tidak valid! Ketik: Merah, Kuning, atau Hijau")
        except (ValueError, KeyboardInterrupt):
            print_delay("❌ Input tidak valid!")


def tahap_lanjut_gunung_1(nama, nyawa):
    """Tahap lanjut path Gunung Bug - Pilihan pertama benar"""
    print("\n" + "=" * 50)
    print_delay("⭐ TAHAP BERIKUTNYA ⭐")
    print("=" * 50)
    print_delay(f"\n✅ {nama} memilih pintu Kuning yang tepat!")
    print_delay(f"❤️  Nyawa: {nyawa}")
    print_delay("\nAnda memasuki ruangan yang penuh dengan cahaya.")
    print_delay("Di sini ada perpustakaan kuno berisi buku-buku programming.")
    print_delay("\nTiba-tiba, seorang roh perangkat lunak muncul!")
    print_delay("Dia memberi Anda satu pertanyaan:")
    print_delay("'Apa itu loop dalam programming?'")
    print_delay("\n1️⃣  Struktur yang mengulang kode hingga kondisi terpenuhi")
    print_delay("2️⃣  Sebuah variabel yang menyimpan angka")
    print()
    
    while True:
        try:
            pilihan = input("Jawaban Anda (1 atau 2): ").strip()
            
            if pilihan == "1":
                return game_over_positif(nama, "Gunung Bug", nyawa)
            elif pilihan == "2":
                nyawa -= 20
                if nyawa <= 0:
                    return game_over_habis_nyawa(nama)
                print_delay(f"\n❌ Jawaban salah! Nyawa berkurang 20.")
                print_delay(f"❤️  Sisa Nyawa: {nyawa}")
                print("\n" + "=" * 50)
                return game_over_negatif(nama, "Roh itu marah dengan jawaban salah Anda!", nyawa)
            else:
                print_delay("❌ Pilihan tidak valid!")
        except (ValueError, KeyboardInterrupt):
            print_delay("❌ Input tidak valid! Silakan masukkan 1 atau 2.")


def game_over_habis_nyawa(nama):
    """Menampilkan game over karena nyawa habis"""
    print("\n" + "=" * 50)
    print_delay("💀 NYAWA HABIS! GAME OVER! 💀")
    print("=" * 50)
    print_delay(f"\n{nama} telah kehabisan nyawa...")
    print_delay("\nAnda kalah dalam petualangan ini.")
    print_delay("\n🔄 Coba lagi dan buat pilihan yang lebih bijaksana!")
    return False


def game_over_negatif(nama, alasan, nyawa):
    """Menampilkan game over dengan cerita negatif"""
    print("\n" + "=" * 50)
    print_delay("❌ GAME OVER ❌")
    print("=" * 50)
    print_delay(f"\n{alasan}")
    print_delay(f"\n💀 Petualangan {nama} berakhir di sini.")
    print_delay(f"❤️  Sisa Nyawa: {nyawa}")
    print_delay("\n🔄 Coba lagi untuk menemukan jalan yang benar!")
    return False


def game_over_positif(nama, lokasi, nyawa):
    """Menampilkan game over dengan cerita positif"""
    print("\n" + "=" * 50)
    print_delay("✨ SELAMAT! ANDA MENANG! ✨")
    print("=" * 50)
    
    if lokasi == "Lembah Coding":
        print_delay(f"\n🎉 {nama} berhasil menguasai ilmu programming!")
        print_delay("Anda menemukan harta karun pengetahuan yang sesungguhnya.")
        print_delay("Kode Anda berjalan sempurna tanpa bug!")
        print_delay("\n🏆 Anda adalah MASTER PROGRAMMER! 🏆")
    elif lokasi == "Gunung Bug":
        print_delay(f"\n🎉 {nama} berhasil melewati semua tantangan!")
        print_delay("Roh perangkat lunak memberikan Anda kekuatan supernatural.")
        print_delay("Anda dapat menulis kode yang sempurna selamanya!")
        print_delay("\n🏆 Anda adalah PEMENANG PETUALANGAN! 🏆")
    
    print_delay(f"❤️  Nyawa tersisa: {nyawa}")
    print()
    return True


def main():
    """Fungsi utama untuk menjalankan game"""
    tampilkan_judul()
    
    nama = ambil_nama_pemain()
    nyawa = 100  # Inisialisasi nyawa pemain
    tampilkan_intro(nama, nyawa)
    
    # Jalankan game
    hasil = pilihan_awal(nama, nyawa)
    
    # Tanyakan apakah ingin bermain lagi
    print("\n" + "=" * 50)
    while True:
        try:
            mainkan_lagi = input("\nMain lagi? (y/n): ").strip().lower()
            if mainkan_lagi in ["y"]:
                main()  # Mulai game baru
                return
            elif mainkan_lagi in ["n"]:
                print_delay("\n👋 Terima kasih telah bermain Mystery Adventure Bot!")
                print_delay("Sampai jumpa lagi!\n")
                return
            else:
                print_delay("❌ Masukkan 'y' atau 'n'")
        except (ValueError, KeyboardInterrupt):
            print_delay("\n❌ Input tidak valid!")


# Menjalankan game
if __name__ == "__main__":
    main()


#2. Ya, pernah.
#kdang AI memberi kode yang error atau tidak lengkap.
#cara memperbaikinya:
#jalankan kode di terminal
#llihat pesan error
#kirim prompt: “Perbaiki kode ini agar tidak error”

#3. menurutku yang lebih sulit adalah logika cerita.
#sintaks Python bisa dibantu AI, klau logika cerita tidak jelas, game jadi membingungkan.
#jadi logika = sumber kreatif
#sintaks = teknik coding
