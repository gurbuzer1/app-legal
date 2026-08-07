# Para yolu — karar: **K1 uygulanmaz — bu bir ürün değil, ALTYAPI**

Fabrika kapısının K1 şartı her **ürün** için ya çalışan bir para yolu ya da
açık bir "sonsuza dek ücretsiz" kararı istiyor. Bu depo ikisini de gerektirmiyor,
çünkü satılacak ya da ücretsiz verilecek bir ürün değil: portföydeki app'lerin
**gizlilik ve destek sayfalarını** barındıran statik bir site.

## Ölçülen durum (2026-08-07)

| | |
|---|---|
| Senkron | 12 commit · origin ile 0/0 |
| İçerik | **20 app dizini** + `index.html` + `destek.html` |
| Yayın | 🟢 **canlı** — `gurbuzer1.github.io/app-legal/` → **200** |
| Örnek sayfa | `…/decideforus/privacy.html` → **200** |
| Ödeme yolu | yok (ve olması anlamsız) |

## Neden K1 uygulanmaz

Bu depo kullanıcıya bir işlev sunmuyor; **Apple'ın zorunlu tuttuğu bağlantıları
karşılıyor.** App Store gönderiminde her app'in bir gizlilik politikası URL'si
olmak zorunda ve o URL'nin **200 dönmesi** gerekiyor. Bu site tam olarak o işi
yapıyor.

Bir gizlilik sayfasına paywall koymak, kuralın kendisini bozardı: kullanıcı
ürünün verisini nasıl işlediğini **ücretsiz** okuyabilmeli.

## 🚨 Ama bu depo SESSİZ BİR TEK NOKTA ARIZASI

K1'in konusu değil, ama daha önemli olabilir: **20 app'in gizlilik ve destek
bağlantısı bu tek statik siteye bağlı.**

Portföyde bunun ne demek olduğu ölçülmüştü: `DecideForUs 1.0.2`'nin gizlilik
linki bir dönem **ölüydü** ve app canlıyken kullanıcı boş sayfa görüyordu; ASC
alanı 409 ile kilitli olduğu için düzeltme **yeni sürüm** gerektirdi.

Yani buradaki bir kırılma, App Store'daki app'lerin **metadata'sını** bozuyor ve
düzeltmesi app tarafında yeni sürüm isteyebiliyor.

Bu yüzden bu depo için doğru "para" kararı şu: **ücretsiz olması gerekli değil,
AYAKTA olması gerekli.** Ölçülmesi gereken şey fiyat değil, **erişilebilirlik**.

## Bu kararın anlamı

- Paywall, reklam, izleme: **hiçbiri eklenmeyecek**. Bir gizlilik sayfasına
  izleyici koymak, sayfanın kendi metnini yalanlar.
- Bu depo bir ürün gibi sıraya alınmayacak; **bağımlılık** olarak izlenecek.

## Sıra

1. **Ayakta kalma ölçümü kurulmalı**: 20 dizinin her birindeki `privacy.html`
   ve varsa `support.html` **200 dönüyor mu** — düzenli olarak. Bugün kök ve bir
   örnek ölçüldü (ikisi de 200), **20'nin tamamı ölçülmedi.**
2. ASC'deki gizlilik URL'leri bu sitedeki gerçek yollarla **karşılaştırılmalı**:
   bir app'in ASC'de yazdığı adres burada yoksa, bağlantı ölü demektir ve bunu
   yalnızca karşılaştırma ortaya çıkarır.
3. GitHub Pages'in kendisi bir bağımlılık — barındırma değişirse 20 app birden
   etkilenir.
