# article

Method | URL                    | remark
------ | ---------------------- | ------------------
GET    | /api/articles          | 获取文章列表
POST   | /api/articles          | 创建一个新的文章
GET    | /api/articles/`<path>` | 获取指定文章文章
PUT    | /api/articles/`<path>` | 更新指定 path 的文章
PATCH  | /api/articles/`<path>` | 对指定 path 的文章进行部分更新
DELETE | /api/articles/`<path>` | 删除指定 path 的文章

---

# setting

Method | URL                    | remark
------ | ---------------------- | ----------------
GET    | /api/settings/         | 获取所有设置
POST   | /api/settings/         | 添加新配置
GET    | /api/settings/`<name>` | 获取指定的配置
PUT    | /api/settings/`<name>` | 更新指定的配置
<!-- PATCH  | /api/settings/`<name>` | 对指定 name 的配置进行更新 -->
DELETE | /api/settings/`<name>` | 删除指定 name 的配置
