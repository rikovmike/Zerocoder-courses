import scrapy


class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://divan.ru/category/svet"]

    def parse(self, response):

       # Создаём переменную, в которую будет сохраняться информация
       # Пишем ту же команду, которую писали в терминале
       svets = response.css('div._Ud0k')
       # Настраиваем работу с каждым отдельным диваном в списке
       for svet in svets:
           # Используем новый для нас оператор "yield", который помогает обрабатывать одно отдельное действие
           # С его помощью мы можем управлять потоком выполнения, останавливать и возобновлять работу парсера
           # С другими операторами мы такого делать не можем
           yield {
           # Ссылки и теги получаем с помощью консоли на сайте
           # Создаём словарик названий, используем поиск по диву, а внутри дива — по тегу span
           'name' : svet.css('div.lsooF span::text').get(),
           # Создаём словарик цен, используем поиск по диву, а внутри дива — по тегу span
           'price' : svet.css('div.pY3d2 span::text').get(),
           # Создаём словарик ссылок, используем поиск по тегу "a", а внутри тега — по атрибуту
           # Атрибуты — это настройки тегов
           'url' : svet.css('a').attrib['href']
           }