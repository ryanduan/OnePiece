#One Piece API

这只是一个API层的小例子，随便写着玩玩。

# [PEP8编码规范](https://github.com/ryanduan/music_api/pep8.md)

##简介 Introduction

###实现功能

假设存储中有完整的海贼王漫画、动画和音乐，而且还在持续的更新中...

首先，我们需要把刚刚更新的内容保存起来，那么，假设我们有完整的图片保存API、视频保存API和音乐保存API，我们这里要做的只是记录他们保存的地址和他们的信息。

其次，我们需要把保存的内容展现出来，这里是以JSON包的形式返回给上层的。当然，我们假设这是给我们的APP提供数据的，网站的话，当然还是假设我们有完整的模板渲染，忽略吧，哈哈。

总的来说，就是一个提供海贼王漫画、动漫和音乐的接口。

###设计思路

假设，我们一天的PV只有几十个，几百个，几千个，几万个...千万个（做梦了），mysql当然可以满足一切需求，但是量级打了，还是需要用用memcached、mongodb、redis来傻傻的缓存一下。

好，定下来了，mysql做存储，redis做缓存。（漫画之类的，画好了谁会改，所以缓存不需要过期时间）

那么处理流程大概就是：

不需要缓存的流程:

Request --> Handler(Controller) --> Mysql --> Response

有缓存的流程:

Request --> Handler(Controller) --> Redis -cached-> Response

需要缓冲没有缓存的流程:

Request --> Handler(Controller) --> Redis -no_cached-> Mysql -cache-> Response

models层：包含Mysql结构，Redis缓存

dao.py封装了数据库连接，mysql和redis。

现在要考虑用什么连接数据库，redis不用想（自然是redis-py），mysql嘛，MySQLdb？？？这玩意这么久都不更新了，新的branch倒还不错。不过，我们也要跟上潮流，直接上SQLAlchemy。

那么，用啥框架呢？[Django](https://github.com/django/django.git)？？简单易用，虽然模板渲染慢到骂娘，但我们不渲染模板。该用啥呢？

自然是NB的哥哥FB的[Tornado](https://github.com/tornadoweb/tornado.git)！！！

好，进入正题，整个项目分为Model层models、Controller层controllers。

对这就完了，木有View层啊！！所有的文档在doc，测试在test，写代码不写稳当当也就算了，不写注释和test，你这是坑Die呀！谁敢发布你的代码？？

model.py封装sqlalchemy的engine、session和redis的connection等。

注：tornado是用git submodules clone的，做法去看git

*  [接口一览表](#接口一览表)
*  [通用参数说明](#参数说明)


##接口一览表
| 接口 | 功能 | 说明 |
| ---- |:----:| ---- |
| [/op/create_car](https://github.com/ryanduan/music_api/blob/master/doc/create_car.md) | 创建漫画 |  |
| [/op/create_ani](https://github.com/ryanduan/music_api/blob/master/doc/create_ani.md) | 创建动画 |  |
| [/op/create_music](https://github.com/ryanduan/music_api/blob/master/doc/create_music.md) | 创建音乐 |  |
| [/op/car](https://github.com/ryanduan/music_api/blob/master/doc/create_car.md) | 看漫画 |  |
| [/op/ani](https://github.com/ryanduan/music_api/blob/master/doc/create_car.md) | 看动漫 |  |
| [/op/music/](https://github.com/ryanduan/music_api/blob/master/doc/create_car.md) | 听音乐 |  |

注：暂无

##参数说明
###接口请求相关参数
| 参数 | 类型 | 说明 |
| ---- |:----:| ---- |
| code | int | 状态码，正确：20000，错误：20000+ |
| msg | string | 信息，正确时可为空 |
| data | dict | 数据包 |

注：以上均在一个JSON包里面

###相关参数
本说明中的所有参数用于接口的接收数据和返回数据，交互前请先了解，不要自造参数

| 参数 | 类型 | 说明 |
| ---- |:----:| ---- |
| mid | int | 歌曲ID |


