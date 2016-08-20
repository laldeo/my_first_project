from django.conf.urls import include, url
from django.contrib import admin
#from address.views import hello_world
from address.views import test_html,address_html
from newtest_app.views import newtest_html

urlpatterns = [
    # Examples:
    # url(r'^$', 'AddressBook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'address.views.hello_world', name='hello'),
    url(r'^test_html',test_html,name="thtml"),
    url(r'^address_html',address_html,name="ahtml"),
    url(r'^newtest_html',newtest_html,name='newtest_html'),

]
