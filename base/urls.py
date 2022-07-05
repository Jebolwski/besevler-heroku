from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as authview
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

     
     #!ADMİNİN KİŞİ CRUD İŞLEMLERİ
    path('kisi/ekle/', views.AddPersonView, name="add"),
    path('anasayfa-admin/', views.AdminHomeView, name="admin-home"),
    path('kisi/<int:pk>/', views.LookPersonView, name="lookperson"),
    path('kisi/<int:pk>/sil/', views.DeletePersonView, name="deleteperson"),
    path('kisi/<int:pk>/duzenle/', views.EditPersonView, name="editperson"),
    path('gelen-kutusu-admin/',views.InboxAdminView,name="inbox-admin"), 
    path('gelen-kutusu-admin/<inbox_id>/',views.InboxAdminDeleteView,name="inbox-admin-delete"), 
    path('gelen-kutusu-admin/<inbox_id>/cevapla/',views.InboxAdminResponseView,name="inbox-admin-response"), 

     #!ADMİNİN DUYURU CRUD İŞLEMLERİ
     path("duyurular/",views.Duyurular, name="duyurular"),
     path("duyuru/<int:pk>/",views.DuyuruDetay, name="duyuru-tek"),
     path("duyuru/ekle/",views.DuyuruOlustur, name="duyuru-ekle"),
     path("duyuru/<int:pk>/duzenle/",views.DuyuruDuzenle, name="duyuru-duzenle"),
     path("duyuru/<int:pk>/sil/",views.DuyuruSil, name="duyuru-sil"),
     

     #!GİRİŞ ÇIKIŞ
    path('giris-yap/', views.CustomLoginView, name="login"),
    path('cikis-yap/', LogoutView.as_view(next_page="citizen-home"), name="logout"),

     #!404
    path('bulunamadi/',views.Bulunamadi,name="404-page"),

     
     #!VATANDAŞ EKRANI
    path("iletisim/", views.CitizenContactView, name="citizen-contact"),
    path('kayit-ol/', views.RegisterPersonView, name="register"),
    path('', views.CitizenHomeView, name="citizen-home"),
    path('ayarlar/', views.CitizenSettingsView, name="citizen-settings"),
    path('gelen-kutusu/<user_id>/',views.InboxCitizenView,name="inbox-citizen"),
    path('gelen-kutusu/<inbox_id>/sil/',views.InboxCitizenDeleteView,name="inbox-citizen-delete"),
    path('onerivesikayet/',views.OneriVeSikayet,name="onerivesikayet"),
    path('onerivesikayet-sil/<int:pk>/',views.OneriVeSikayetSil,name="onerivesikayetsil"),
    path('onerivesikayet/<int:pk>/',views.OneriVeSikayetDetay,name="onerivesikayetdetay"),
     
     
     #!ŞİFRE İŞLEMLERİ
    path('sifre-sifirla/', authview.PasswordChangeView.as_view(template_name="base/password/passwordreset.html"),
         name="change_password"),
    path('sifre-sifirla-bitti/', authview.PasswordChangeDoneView.as_view(template_name="base/password/passwordresetdone1.html"),
         name="password_change_done"),
    path('sifre-sifirla-gonderildi/',
         authview.PasswordResetDoneView.as_view(template_name="base/password/passwordresetdone.html"), name="password_reset_done"),
    path('sifre-sifirla/<uidb64>/<token>/',
         authview.PasswordResetConfirmView.as_view(template_name="base/password/passwordresetemail.html"), name="password_reset_confirm"),
    path('sifre-sifirlandı/', authview.PasswordResetCompleteView.as_view(template_name='base/password/resetcomplete.html'),
         name="password_reset_complete"),
    path('sifre-unuttum/', authview.PasswordResetView.as_view(template_name="base/password/passwordforgotreset.html"),
         name="password_forgot_reset"),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
