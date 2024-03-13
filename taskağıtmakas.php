<?php

// Oyun fonksiyonu
function oyun($oyuncuSecim) {
  // Bilgisayar seçimi
  $bilgisayarSecim = rand(0, 2);

  // Kazananı belirleme
  $kazanan = ($oyuncuSecim - $bilgisayarSecim + 3) % 3;

  // Sonuçları yazdırma
  echo "**Oyuncu Seçimi:** " . secimStr($oyuncuSecim) . "<br>";
  echo "**Bilgisayar Seçimi:** " . secimStr($bilgisayarSecim) . "<br>";

  if ($kazanan == 0) {
    echo "**Berabere!**<br>";
  } elseif ($kazanan == 1) {
    echo "**Tebrikler, kazandınız!**<br>";
  } else {
    echo "**Maalesef, kaybettiniz!**<br>";
  }

  return $kazanan;
}

// Seçim stringi
function secimStr($secim) {
  switch ($secim) {
    case 0:
      return "Taş";
    case 1:
      return "Kağıt";
    case 2:
      return "Makas";
  }
}

// Oyun başlangıcı
$oyuncuSkor = 0;
$bilgisayarSkor = 0;

define('STDIN', fopen('php://stdin', 'r')); // Tanımlama eklendi

for ($i = 0; $i < 3; $i++) {
  // Oyuncu seçimi
  $oyuncuSecim = -1;
  while ($oyuncuSecim < 0 || $oyuncuSecim > 2) {
    echo "Seçiminizi giriniz (0=Taş, 1=Kağıt, 2=Makas): ";
    $oyuncuSecim = trim(fgets(STDIN));
  }

  // Oyun oynama
  $kazanan = oyun($oyuncuSecim);

  // Skor güncelleme
  if ($kazanan == 1) {
    $oyuncuSkor++;
  } elseif ($kazanan == 2) {
    $bilgisayarSkor++;
  }
}

// Sonuçları gösterme
echo "**Oyuncu Skor:** " . $oyuncuSkor . "<br>";
echo "**Bilgisayar Skor:** " . $bilgisayarSkor . "<br>";

if ($oyuncuSkor > $bilgisayarSkor) {
  echo "**Tebrikler, oyunu kazandınız!**";
} elseif ($oyuncuSkor < $bilgisayarSkor) {
  echo "**Maalesef, oyunu kaybettiniz!**";
} else {
  echo "**Oyun berabere!**";
}

// Tekrar oynama isteği
$tekrarOyna = "";
while ($tekrarOyna != "E" && $tekrarOyna != "H") {
  echo "Tekrar oynamak ister misiniz? (E/H): ";
  $tekrarOyna = trim(fgets(STDIN));
}

if ($tekrarOyna == "E") {
  echo "**Tekrar oynuyorsunuz...**<br>";
  header("Location: " . $_SERVER['PHP_SELF']);
} else {
  echo "**Teşekkürler, tekrar görüşmek üzere!**";
}

?>
