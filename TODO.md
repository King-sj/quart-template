# TODO
- [ ] 兼容 args 和 ENV 两种方式
- [ ] 解决多个test并行的问题('cannot perform operation: another operation is in progress',)
- [ ] 研究为什么 Hypercorn 不能正常使用
- [ ] aioredis 不能正确适配 python3.13 的问题
- [ ] 支持各种数据库驱动
  - [ ] postgreSQL
  - [ ] mysql
  - [ ] redis
  - [ ] redis in file/memory (自己实现一个库?)
  - [ ] relational database in file/memory(自己实现一个库?)
- [ ] 支持JWT生成无状态TOKEN, OAuth 做权限管理， 目前是自己实现的有状态TOKEN, 不适合分布式系统
- [ ] 引入ORM(Object Relational Mapping) 简化部分SQL使用【sqlalchemy，Tortoise ORM,Pony ORM】
- [ ] 基于Redis实现分布式锁
- [ ] 考虑是否引入微服务架构
- [ ] 考虑引入GraphQL

## 解决 Tortoise 调试报错的问题
<!-- 貌似是由asyncpg 导致的 ???-->
这种会报错InterfaceError('cannot perform operation: another operation is in progress')

@pytest.mark.asyncio
async def test_user(client):
