# Disk网盘（名称待定）操作指南

### 工刀180112，于圣何塞

## 崭新的设计
整个系统的每个部分都用了对我而言崭新的设计。
#### 后端
依旧是Django框架，但重构了之前积累的基础代码。

- 使用jwt模块代替session，减轻服务器压力，把口令（token）通过HTTP请求头传送。
- 传入参数预检验原先只用了简单的装饰器，只检查是否存在某个参数，而没有对参数的值进行检查。新设计的装饰器支持快捷正则判断、自定义检验函数、添加默认值、参数预处理。详见`Base.decorator`模块。
- 把针对数据库操作（增删改查）和异常都包装在models中，把绝大部分的模型方法的返回值都使用新的返回类`Ret`，并和`error_response`错误回复无缝衔接。
- 模型方法支持属性值检测（使用`models.L`检测属性的长度，`R_TUPLE`检测属性值是否合法等），且支持自定义检测函数（`_valid_R`格式）。
- 使用七牛前端口令上传并回调，使用CDN存储数据。
- 遵循PEP8代码风格。

#### 服务器
- 使用nginx+gunicorn代替apache+uwsgi方案，目测支持多域名多项目方案。

#### 前端
- 首次使用angular4框架，前后端完全分离，使用跨域请求。


## API文档
API的设计尽可能的贴近了RestAPI的设计，并通过一定方式保护数据。
