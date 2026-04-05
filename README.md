

👥 Takım Üyeleri
Muhammed Emin Saylağ

Anıl Başoğlu

Emre Balcan

🛠 Uygulanan Teknik Süreçler
1. Dal Koruma (Branch Protection)
main dalı doğrudan push işlemlerine karşı korumaya alınmıştır. Tüm değişiklikler Pull Request (PR) mekanizması ve kod incelemesi (Code Review) ile birleştirilmiştir.

Hata Simülasyonu: main dalına direkt push denendiğinde GH006: Protected branch update failed hatası alınarak korumanın çalıştığı doğrulanmıştır.

2. Çatışma Senaryosu (Conflict Resolution)
Aynı dosyanın (algoritma.py) aynı satırında iki farklı üye tarafından değişiklik yapılarak bilinçli bir çatışma oluşturulmuştur.

Çözüm Yöntemi: Çatışma hem GitHub UI üzerinden hem de yerel terminalde git merge komutuyla, <<<<<<<, =======, >>>>>>> işaretleri temizlenerek çözülmüştür.

3. Rebase Deneyi (Advanced Git)
Projenin geçmişini daha temiz ve doğrusal (linear) tutmak için rebase tekniği uygulanmıştır.

Komut: git rebase main

Sonuç: Karmaşık dal yapısı yerine, commit geçmişi tek bir düz çizgi haline getirilmiştir. Geçmiş yeniden yazılarak (Rewrite History) temiz bir log elde edilmiştir.
⚠️ Hata Kurtarma Simülasyonları
Proje sürecinde aşağıdaki senaryolar üzerinde çalışılmıştır:

git commit --amend: Hatalı yazılan commit mesajları düzeltildi.

git reset --soft/hard: Yanlışlıkla atılan commit'ler geri alındı.

git reflog: Kaybolan veya silinen commit'lerin izi sürülerek geri getirme provası yapıldı.

git restore: Kaydedilmemiş dosya değişiklikleri eski haline döndürüldü.

📊 Proje Yönetimi
Süreç boyunca aşağıdaki GitHub araçları aktif olarak kullanılmıştır:

GitHub Issues: Görev dağılımı ve bug takibi yapıldı.

GitHub Projects: İşlerin durumu (To Do, In Progress, Done) Kanban board üzerinde görselleştirildi.

🎓 Kazanımlarımız
Merge vs Rebase: Merge'in geçmişi koruduğunu, Rebase'in ise daha temiz bir tarihçe sunduğunu deneyimledik.

Branch = Pointer: Dalların sadece birer işaretçi olduğunu ve Git'in ne kadar hızlı çalıştığını anladık.

Conflict: Çatışmaların bir hata değil, ekip çalışmasının doğal bir parçası olduğunu öğrendik.
