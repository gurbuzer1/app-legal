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

## ✅ Tam ölçüm yapıldı (2026-08-07) — ve asıl bulgu BAŞKA YERDEYDİ

Önceki turda "20'nin tamamı ölçülmedi" diye sıraya yazılmıştı. Yapıldı:

**1) Bu sitedeki her sayfa** — 20 dizindeki `privacy.html` / `support.html`
dosyalarının **hepsi 200**. Tek bir ölü sayfa yok.

**2) Üç dizinde `privacy.html` YOK** (`caniai`, `forget-me-not`, `skillquest`)
ve o yollar gerçekten **404** veriyor. Ama ölü bağlantı **değiller**: ölçüm
ASC'ye kadar götürülünce üçünün de kendi alan adını beyan ettiği görüldü
(`caniai.vercel.app/privacy`, `gurbuzer1forget-me-not.vercel.app/privacy`,
`skillquest.46-225-185-206.nip.io/privacy`) — üçü de **200**.
⚠️ Yani "dosya yok" tek başına bulgu değildi; bulgu ancak **ASC'nin ne
beyan ettiğiyle karşılaştırınca** ortaya çıkar ya da çıkmaz.

**3) 27 app'in TAMAMININ beyan ettiği gizlilik URL'si çağrıldı: 26'sı 200.**

🔴 **Dönmeyen tek app: `Decide For Us` — App Store'da CANLI olan iki app'ten
biri.** `decideforus.app` DNS'te çözülüyor (`198.54.117.242`, park IP'si) ama
TLS 443 **ECONNREFUSED**; `/privacy`, `/` ve `www.*` üçü de **000**. Çalışan
sayfa bu sitede duruyor (`…/app-legal/decideforus/privacy.html` → 200) ama ASC
oraya bakmıyor.

Ayrıntı ve düzeltme yolu: canonical `decideforus` deposunun `PARA.md`'sinde
(`0d92716`). Özet: ASC alanı donmuş (`READY_FOR_SALE`, düzenlenebilir `appInfo`
yok), **doğru çözüm alan adını yeniden yayına almak** — yeni sürüm gerekmiyor.

İki app'in (`Helal Barkod`, `Aktüel Takip`) beyan edilmiş gizlilik URL'si
**hiç yok**; ikisi de zaten yayın engeli yazılı olanlar.

## Sıra

1. ✅ Ayakta kalma ölçümü **yapıldı** (yukarıda). Tekrarlanabilir olması için
   düzenli koşum kalıyor.
2. ✅ ASC karşılaştırması **yapıldı** — ve tek gerçek bulguyu o ortaya çıkardı.
3. GitHub Pages'in kendisi bir bağımlılık — barındırma değişirse 20 app birden
   etkilenir.
