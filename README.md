# Zen

## API 文档

Zen 当前提供以下 API：

## Authentication API

### 注册用户

`POST /register`

请求：

```json
{
  "username": "admin",
  "password": "123456"
}
```

返回：

```json
{
  "id": 1,
  "username": "admin"
}
```

---

### 用户登录

`POST /login`

请求：

```json
{
  "username": "admin",
  "password": "123456"
}
```

返回 JWT Token：

```json
{
  "access_token": "xxxxx",
  "token_type": "bearer",
  "user_id": 1,
  "username": "admin"
}
```

---

## API Key 管理

### 创建 API Key

`POST /create`

请求：

```json
{
  "user_id": 1,
  "name": "default"
}
```

返回：

```json
{
  "api_key": "zen_xxxxx",
  "name": "default"
}
```

说明：

- API Key 明文只返回一次
- 数据库存储 SHA256 Hash
- 支持用户级 API Key 管理

---

### 查询 API Key

`GET /list/{user_id}`

返回用户所有 Key 信息：

```json
[
  {
    "id": 1,
    "name": "default",
    "key_prefix": "zen_xxxxx",
    "is_active": 1
  }
]
```

---

### 禁用 API Key

`DELETE /{key_id}`

返回：

```json
{
  "deleted": true
}
```

---

## 技术栈

- FastAPI
- SQLite
- JWT Authentication
- API Key Management
- Cloudflare Workers Support
- uv Package Manager

## Deployment

Cloudflare Workers:

```bash
uv sync
uv run pywrangler deploy
```

Local:

```bash
uv run python run_local.py
```
