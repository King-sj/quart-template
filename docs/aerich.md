1. **安装 Tortoise ORM**： 在您的项目中安装 Tortoise ORM 和相关依赖：

  ```sh
  pip install tortoise-orm
  ```

2. **配置 Tortoise ORM**： 在项目中创建一个新的配置文件 `tortoise_config.py`，并配置数据库连接和模型路径：

  ```python
  # src/tortoise_config.py
  TORTOISE_ORM = {
     "connections": {
         "default": "postgres://postgres:postgres@localhost:5432/postgres"
     },
     "apps": {
         "models": {
             "models": ["src.models", "aerich.models"],
             "default_connection": "default",
         },
     },
  }
  ```

3. **定义 Tortoise ORM 模型**：

  ```python
  # src/models/user.py
  from tortoise import fields
  from tortoise.models import Model

  class User(Model):
     id = fields.BigIntField(pk=True)
     email = fields.CharField(max_length=255, unique=True)
     password = fields.CharField(max_length=255)
     created_at = fields.DatetimeField(auto_now_add=True)
     is_deleted = fields.BooleanField(default=False)
     deleted_at = fields.DatetimeField(null=True)
     role = fields.CharField(max_length=255, null=True)
     name = fields.CharField(max_length=255, null=True)

     def __str__(self):
         return self.email
  ```

4. **初始化 Tortoise ORM**： 在

create_app

函数中初始化 Tortoise ORM：

```python
# src/app.py
   from tortoise.contrib.quart import register_tortoise

   def create_app():
       app = Quart(__name__, static_folder='../static')
       app = cors(app, allow_origin=args.allow_origin)

       register_tortoise(
           app,
           db_url="postgres://postgres:postgres@localhost:5432/postgres",
           modules={"models": ["src.models"]},
           generate_schemas=True,
           add_exception_handlers=True,
       )

       register_blueprints(app)

       return app
```

1. **迁移工具 Aerich**： 安装 Aerich 以管理数据库迁移：

  ```sh
  pip install aerich
  ```

2. **初始化 Aerich**： 初始化 Aerich 配置：

  ```sh
  aerich init -t src.tortoise_config.TORTOISE_ORM
  aerich init-db
  ```

3. **创建迁移文件**： 当您对模型进行更改时，使用 Aerich 创建迁移文件：

  ```sh
  aerich migrate
  aerich upgrade
  ```

4. **更新测试和其他代码**： 更新测试和其他代码以使用 Tortoise ORM 进行数据库操作。
