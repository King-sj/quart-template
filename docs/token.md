### 1. Flask/Quart 如何实现 API 网关（验证 Token/鉴权）

**实现步骤**：
- **中间件/装饰器**：通过 `before_request` 钩子或装饰器拦截请求，统一处理鉴权。
- **Token 提取**：从请求头（如 `Authorization: Bearer <token>`）或 Cookie 中提取 Token。
- **Token 验证**：
  - **JWT 验证**：使用库（如 `pyjwt` 或 `Flask-JWT-Extended`）验证签名、过期时间和合法性。
  - **状态 Token 检查**：若为有状态 Token（如 Session ID），需查询数据库/缓存验证有效性。
- **鉴权逻辑**：
  - 从 Token 中解析用户角色/权限（如 JWT 的 `payload.roles`）。
  - 对比请求路径与用户权限（如 RBAC 模型），无权限则返回 `403 Forbidden`。
- **集成方案**：
  - 结合 OAuth2.0（使用 `authlib` 库）或 OpenID Connect。
  - 使用 API 网关框架（如 Kong、Typhoeus）或自定义轻量级网关。

---

### 2. Token 应该无状态还是有状态？

- **无状态 Token（如 JWT）**：
  - **优点**：扩展性强，适合分布式系统；服务端无需存储状态。
  - **缺点**：难以主动吊销，需依赖短有效期或黑名单机制。
- **有状态 Token（如 Session ID）**：
  - **优点**：服务端可主动控制会话（如强制退出）。
  - **缺点**：需维护会话存储，增加系统复杂性。
- **结论**：无状态 Token 是现代 API 的主流选择，但需结合业务需求。高安全性场景可混合使用（如 JWT + 黑名单）。

---

### 3. JWT B/S 端各保存的信息

- **客户端（Browser/Client）**：
  - 存储整个 JWT（通常通过 `localStorage`、`sessionStorage` 或 Cookie）。
  - 包含 `Header`（算法）、`Payload`（用户 ID、角色、过期时间等）和 `Signature`。
- **服务端（Server）**：
  - **不存储 JWT 内容**（依赖签名验证有效性）。
  - 可能存储吊销列表（如 Redis 记录失效 Token）或密钥（用于签名验证）。
  - 需要保存生成 JWT 的密钥（如 HS256 的密钥或 RS256 的私钥）。

---

### 4. 常见最佳实践

- **安全传输**：强制使用 HTTPS，避免 Token 泄露。
- **短有效期**：访问令牌（Access Token）设置较短过期时间（如 15 分钟）。
- **Refresh Token**：用于获取新 Access Token，存储于安全位置（如 HttpOnly Cookie）。
- **最小化 Payload**：避免在 JWT 中存储敏感信息。
- **签名算法**：使用 RS256（非对称加密）替代 HS256（对称加密），防止密钥泄露。
- **吊销机制**：通过黑名单或数据库维护失效 Token（适用于关键操作）。
- **标准化协议**：优先采用 OAuth2.0/OpenID Connect，而非自定义鉴权。

---

### 5. 去中心化集群的节点 IP 发现机制

- **服务发现工具**：
  - **Consul/etcd/ZooKeeper**：节点启动时注册，其他节点查询服务目录。
  - **Kubernetes 服务发现**：通过 `Service` 和 `kube-dns` 自动管理内网 DNS。
- **DNS 轮询**：配置 DNS 返回多个节点 IP（简单但缺乏健康检查）。
- **Gossip 协议**：节点间通过 P2P 广播交换存活信息（如 Cassandra 使用）。
- **种子节点（Seed Nodes）**：硬编码初始节点 IP，新节点通过种子获取集群列表。
- **云原生方案**：AWS 的 Cloud Map、阿里云 Nacos 等托管服务。

---

**总结**：现代分布式系统倾向于结合无状态 Token（JWT）和自动化服务发现（如 Kubernetes + Consul），同时遵循 OAuth2.0 和短有效期 Token 的最佳实践，以平衡安全性与扩展性。