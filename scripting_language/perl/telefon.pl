use strict;
use warnings;
use utf8;
use open ':std', ':encoding(UTF-8)';

# ===============================
# VECTOR (ARRAY) WITH RAW DATA
# ===============================
my @data = (
    "1\t5456164158\tMesaj attı\t\t05.09.2022 16:01:39\t80 sn.\tÇAĞRI ŞAHİN",
    "2\t5424784215\tMesaj aldı\t\t05.09.2022 16:01:40\t347 sn.\tMEHMET DEMİRCİ",
    "3\t5439416562\tAradı\t\t\t05.09.2022 16:02:50\t30 sn.\tURAZ YAVANOGLU",
    "4\t5454154545\tMesaj aldı\t\t06.09.2022 11:46:43\t200 sn.\tŞEREF SAĞIROĞLU",
    "5\t5456861654\tArandı\t\t\t06.09.2022 12:47:33\t3 sn.\tMUSTAFA ERDOĞAN",
);

# ===============================
# PARSE + PRINT
# ===============================
foreach my $line (@data) {

    my ($sira, $numara, $tip, $tarih_saat, $sure, $kisi)
        = split /\t+/, $line;

    my ($tarih, $saat) = split / /, $tarih_saat;

    $sure =~ /(\d+)/;
    my $sn = $1;

    my $dakika = int($sn / 60);
    my $saniye = $sn % 60;

    my $sure_yazi = $dakika > 0
        ? "$dakika dakika $saniye saniye"
        : "$saniye saniye";

    print <<"END";
Sıra No: $sira
Kişi: $kisi
Numara: $numara
Arama Tipi: $tip
Arama Tarihi: $tarih
Arama Saati: $saat
Konuşma Süresi: $sure_yazi

END
}
