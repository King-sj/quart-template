## 为什么不使用dataclass
因为想要在tests环境下重新加载.env.tests来覆盖dev/prod环境的变量，实现不影响开发or测试环境，得到一个干净的测试环境