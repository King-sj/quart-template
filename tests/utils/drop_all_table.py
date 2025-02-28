import src.models
from tortoise.models import Model as TortoiseModel
async def drop_all_tables():
  # await User.all().delete()

  # 1. 从 src.models 中导入所有的model
  # 2. 去除不继承from tortoise.models import Model的model
  # 3. 都调用Class.all().delete()方法
  # 获取所有模型类
  model_classes = [
      getattr(src.models, name) for name in dir(src.models)
      if isinstance(getattr(src.models, name), type)
  ]

  # 过滤出继承自 Tortoise Model 的类
  tortoise_models = [
      cls for cls in model_classes if issubclass(cls, TortoiseModel)
  ]

  # 遍历所有 Tortoise ORM 模型并删除所有数据
  for model in tortoise_models:
    # 使用 `model.all().delete()` 清除数据
    await model.all().delete()
