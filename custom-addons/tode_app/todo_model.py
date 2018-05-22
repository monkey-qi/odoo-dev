# -*- coding:utf-8 -*-

from odoo import models, fields, api


# 定义模型类
class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-do Task'
    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)

    # 对于每个级别能处理的选项
    first = fields.Boolean('第一级别是否审批', default=False)
    second = fields.Boolean('第二级别是否审批', default=False)
    third = fields.Boolean('第三级别是否审批', default=False)
    f_is = fields.Boolean('是否审批通过', default=False)
    s_is = fields.Boolean('是否审批通过', default=False)
    t_is = fields.Boolean('是否审批通过', default=False)

    @api.multi
    def do_toggle_done(self):
        for task in self:
            task.is_done = not task.is_done
        return True

    @api.model
    def do_clear_done(self):
        dones = self.search([('is_done', '=', True)])
        dones.write({'active': False})
        return True

        # 判断用户属于哪一个等级
        # @api.model
        # def first(self):
        #     pass
        # 用户为等级一
        # 将first的readonly改为0，则用户只能编辑等级一的审批选项，其他选项处于灰色不可编辑状态

        # @api.model
        # def first(self):
        #     pass
        # 用户为等级二
        # 将second的readonly改为0，则用户只能编辑等级二的审批选项，其他选项处于灰色不可编辑状态

        # @api.model
        # def first(self):
        #     pass
        # 用户为等级二
        # 将second的readonly改为0，则用户只能编辑等级二的审批选项，其他选项处于灰色不可编辑状态
