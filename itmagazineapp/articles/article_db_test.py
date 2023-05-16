from .models import Article
from users.models import User
from users.user_db_test import prepopulate_db_user

def prepopulate_db_article():

    prepopulate_db_user()

    article_obj = Article.objects.all()

    #annafrancis = User.objects.get(id=2) 
    wrightmurray = User.objects.get(id=4)
    alexanderaleman = User.objects.get(id=7)
    toniamin = User.objects.get(id=8)
    arneyblake = User.objects.get(id=10)

    if not article_obj:

        article01 = Article.objects.create( 
            user = arneyblake, 
            headline = 'Ut sodales lectus eget justo maximus',
            description = 'Nunc vitae finibus neque. Proin sed ornare velit, placerat dapibus lectus. Nam in magna ullamcorper, suscipit sapien rutrum, ultricies mi. Nam eget purus fermentum, rutrum justo vel, consectetur dui.',
            body = 'Nulla faucibus ante nisi, at convallis mauris pulvinar a. Suspendisse nec feugiat lorem. Donec at lectus dapibus, auctor enim quis, pulvinar magna. In ac odio interdum, molestie massa nec, sodales metus. Vivamus nec felis a dolor commodo tempus vitae eget risus. Sed nec libero sed velit faucibus lobortis sed nec mi. Praesent felis lectus, convallis at mi id, porttitor ullamcorper augue. In posuere velit quis dolor dictum ullamcorper. Aenean fringilla libero mattis, fringilla enim sed, dignissim elit. Sed non erat porta, gravida augue ac, semper lectus. Maecenas fringilla fermentum risus, sed dignissim leo lobortis sed. Aliquam erat volutpat.',
            location = 'Anchorage'
            )
        
        article02 = Article.objects.create( 
            user = wrightmurray, 
            headline = 'Pellentesque orci nunc, pulvinar sit amet pharetra at, maximus eget erat.',
            description = 'Pellentesque orci nunc, pulvinar sit amet pharetra at, maximus eget erat. Sed imperdiet mi libero, ullamcorper pulvinar massa feugiat id.',
            body = 'Nulla faucibus ante nisi, at convallis mauris pulvinar a. Suspendisse nec feugiat lorem. Donec at lectus dapibus, auctor enim quis, pulvinar magna. In ac odio interdum, molestie massa nec, sodales metus. Vivamus nec felis a dolor commodo tempus vitae eget risus. Sed nec libero sed velit faucibus lobortis sed nec mi. Praesent felis lectus, convallis at mi id, porttitor ullamcorper augue. In posuere velit quis dolor dictum ullamcorper. Aenean fringilla libero mattis, fringilla enim sed, dignissim elit. Sed non erat porta, gravida augue ac, semper lectus. Maecenas fringilla fermentum risus, sed dignissim leo lobortis sed. Aliquam erat volutpat.',
            location = 'Kabul'
            )
        
        article03 = Article.objects.create( 
            user = alexanderaleman, 
            headline = 'Etiam consectetur iaculis metus, et dictum purus bibendum ac.',
            description = 'Vivamus nec felis a dolor commodo tempus vitae eget risus. Sed nec libero sed velit faucibus lobortis sed nec mi. Praesent felis lectus, convallis at mi id, porttitor ullamcorper augue.',
            body = 'Nulla faucibus ante nisi, at convallis mauris pulvinar a. Suspendisse nec feugiat lorem. Donec at lectus dapibus, auctor enim quis, pulvinar magna. In ac odio interdum, molestie massa nec, sodales metus. Vivamus nec felis a dolor commodo tempus vitae eget risus. Sed nec libero sed velit faucibus lobortis sed nec mi. Praesent felis lectus, convallis at mi id, porttitor ullamcorper augue. In posuere velit quis dolor dictum ullamcorper. Aenean fringilla libero mattis, fringilla enim sed, dignissim elit. Sed non erat porta, gravida augue ac, semper lectus. Maecenas fringilla fermentum risus, sed dignissim leo lobortis sed. Aliquam erat volutpat.',
            location = 'Busan'
            )
        
        article04 = Article.objects.create( 
            user = arneyblake, 
            headline = 'Aenean eu erat non purus maximus porttitor id vel ante.',
            description = 'Mauris lectus tellus, malesuada faucibus ipsum et, vulputate vulputate magna. Mauris et tortor dolor.',
            body = 'Nulla faucibus ante nisi, at convallis mauris pulvinar a. Suspendisse nec feugiat lorem. Donec at lectus dapibus, auctor enim quis, pulvinar magna. In ac odio interdum, molestie massa nec, sodales metus. Vivamus nec felis a dolor commodo tempus vitae eget risus. Sed nec libero sed velit faucibus lobortis sed nec mi. Praesent felis lectus, convallis at mi id, porttitor ullamcorper augue. In posuere velit quis dolor dictum ullamcorper. Aenean fringilla libero mattis, fringilla enim sed, dignissim elit. Sed non erat porta, gravida augue ac, semper lectus. Maecenas fringilla fermentum risus, sed dignissim leo lobortis sed. Aliquam erat volutpat.',
            location = 'Fortaleza'
            )
        
        article05 = Article.objects.create( 
            user = toniamin, 
            headline = 'Nunc vitae finibus neque.',
            description = 'Aenean eget enim arcu. Cras id tempus turpis. Sed efficitur augue erat, vel tincidunt magna consequat sit amet.',
            body = 'Nulla faucibus ante nisi, at convallis mauris pulvinar a. Suspendisse nec feugiat lorem. Donec at lectus dapibus, auctor enim quis, pulvinar magna. In ac odio interdum, molestie massa nec, sodales metus. Vivamus nec felis a dolor commodo tempus vitae eget risus. Sed nec libero sed velit faucibus lobortis sed nec mi. Praesent felis lectus, convallis at mi id, porttitor ullamcorper augue. In posuere velit quis dolor dictum ullamcorper. Aenean fringilla libero mattis, fringilla enim sed, dignissim elit. Sed non erat porta, gravida augue ac, semper lectus. Maecenas fringilla fermentum risus, sed dignissim leo lobortis sed. Aliquam erat volutpat.',
            location = 'Daegu'
            )

        print('***Pre-populating articles list***')

    else :

        print('***Articles list pre-populated***')