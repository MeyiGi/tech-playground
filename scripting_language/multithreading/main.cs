using System;
using System.Diagnostics;
using System.Threading;

namespace OdevProjesi
{
    class Program
    {
        // Tüm threadlerin üzerine ekleme yapacağı ortak (global) değişken
        static long toplamSonuc = 0;

        // Kritik bölgeye (Critical Section) giriş çıkış için kullanılacak kilit nesnesi
        static object kilitObjesi = new object();

        static void Main(string[] args)
        {
            // Ödevde istenen 10 milyon sayısı
            long limit = 10000000;
            
            // Tablo başlıklarını yazdıralım (Sola yaslı format)
            Console.WriteLine("{0,-15} {1,-20} {2,-20}", "İplik Sayısı", "Süre", "Sonuç");
            Console.WriteLine("------------------------------------------------------------");

            // 1'den 32 thread'e kadar deneme yapacağız
            for (int i = 1; i <= 32; i++)
            {
                int threadSayisi = i;

                // Her döngüde toplam sonucu sıfırlamamız lazım yoksa üstüne ekler
                toplamSonuc = 0;

                // Süre ölçümü için kronometre başlat
                Stopwatch sureOlcer = new Stopwatch();
                sureOlcer.Start();

                // Threadleri tutacak dizi
                Thread[] isParcaciklari = new Thread[threadSayisi];

                // Her thread'e ne kadar sayı düşecek hesapla
                long parca = limit / threadSayisi;

                for (int j = 0; j < threadSayisi; j++)
                {
                    // Hangi aralığı toplayacağını belirliyoruz
                    long baslangic = (j * parca) + 1;
                    long bitis = baslangic + parca - 1;

                    // Eğer son thread ise, artan kalan sayıları da o alsın (tam bölünmeme durumu)
                    if (j == threadSayisi - 1)
                    {
                        bitis = limit;
                    }

                    // Thread oluşturma kısmı
                    isParcaciklari[j] = new Thread(() => ToplamaIslemi(baslangic, bitis));
                    isParcaciklari[j].Start();
                }

                // Ana programın, tüm threadlerin işini bitirmesini beklemesi lazım (Join)
                for (int k = 0; k < threadSayisi; k++)
                {
                    isParcaciklari[k].Join();
                }

                sureOlcer.Stop();

                // Süreyi saniye cinsinden alıp formatlıyoruz
                string sureYazisi = sureOlcer.Elapsed.TotalSeconds.ToString("0.0000") + " saniye";

                // Sonuçları ekrana bas
                Console.WriteLine("{0,-15} {1,-20} {2,-20}", threadSayisi, sureYazisi, toplamSonuc);
            }

            // Konsol hemen kapanmasın diye
            Console.WriteLine("\nİşlem bitti. Çıkmak için enter'a basın.");
            Console.ReadLine();
        }

        // Threadlerin çalıştırdığı fonksiyon
        static void ToplamaIslemi(long bas, long son)
        {
            long araToplam = 0;

            // Önce kendi aralığındaki sayıları topluyor
            for (long k = bas; k <= son; k++)
            {
                araToplam += k;
            }

            // BURASI KRİTİK BÖLGE (CRITICAL SECTION)
            // Monitor lock mekanizması kullanıyoruz.
            // Aynı anda sadece 1 thread içeri girip global değişkene yazabilir.
            lock (kilitObjesi)
            {
                toplamSonuc = toplamSonuc + araToplam;
            }
        }
    }
}c