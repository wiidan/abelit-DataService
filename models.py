# -*- encoding: utf-8 -*-
'''
@File    :   models.py
@Time    :   2020/03/21 08:31:10
@Author  :   Abelit
@Version :   1.0
@Contact :   ychenid@live.com
@Copyright :   (C)Copyright 2020, dataforum.org
Licence :   BSD-3-Clause
@Desc    :   None
'''


from db import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import uuid


class GiftCardModel(db.Model):
    __tablename__ = "gift_feedback"
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    title_confirmdate = db.Column(db.DateTime, nullable=True, doc="确认回复日期")

    base_brdname = db.Column(db.String(100), unique=True,
                     nullable=False, doc="品牌名称")
    base_shopno = db.Column(db.String(100), nullable=False, doc="店铺号")
    base_company = db.Column(db.String(100), unique=True,
                     nullable=False, doc="品牌名称")
    base_expiredate = db.Column(db.DateTime, nullable=True, doc="活动有效期")

    mem_check = db.Column(db.Integer, nullable=False,doc="是否提供会员福利，1是，0否")
    mem_silverdiscount = db.Column(db.Integer, nullable=False,doc="百合银卡消费折扣")
    mem_gloddiscount = db.Column(db.Integer, nullable=False,doc="玫瑰金卡消费折扣")
    mem_diamonddiscount = db.Column(db.Integer, nullable=False,doc="牡丹钻石卡消费折扣")
    mem_other = db.Column(db.Text, nullable=False,doc="其他增值福利")
    
    sign_signature = db.Column(db.String(100), unique=True,
                     nullable=False, doc="租户签名")
    sign_contact = db.Column(db.String(100), unique=True,
                     nullable=False, doc="联系人")

    sign_call = db.Column(db.String(100), unique=True,
                     nullable=False, doc="联系电话")

    sign_email = db.Column(db.String(100), unique=True,
                     nullable=False, doc="联系电话")

    sign_replydate = db.Column(db.DateTime, nullable=True, doc="活动有效期")
    
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_timestamp = db.Column(
        db.DateTime, nullable=False, onupdate=datetime.now, default=datetime.now)

    def __repr__(self):
        return '<GiftCardModel %r>' % self.name

class ShopCardModel(db.Model):
    __tablename__ = "shop_feedback"
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    title_confirmdate = db.Column(db.DateTime, nullable=True, doc="确认回复日期")
    title_vipperson = db.Column(db.String(100), 
                     nullable=False, doc="致意某人")
    title_vipemail = db.Column(db.String(100),
                     nullable=False, doc="会员管理部邮箱")
    title_viptel = db.Column(db.String(100),
                     nullable=False, doc="会员管理部电话")

    base_brdname = db.Column(db.String(100), unique=True,
                     nullable=False, doc="品牌名称")
    base_shopno = db.Column(db.String(100), nullable=False, doc="店铺号")
    base_company = db.Column(db.String(100), unique=True,
                     nullable=False, doc="品牌名称")

    spcard_check = db.Column(db.Integer, nullable=False,doc="是否接受，1接受，0不接受")
    spcard_shopmall = db.Column(db.Integer, nullable=False,doc="购物中心")
    spcard_dolphin = db.Column(db.Integer, nullable=False,doc="海豚广场")
    spcard_gyint = db.Column(db.Integer, nullable=False,doc="贵阳国际大道")

    remark_policy = db.Column(db.Text, unique=True,
                     nullable=False, doc="优惠政策") 
    remark_contact = db.Column(db.String(100), unique=True,
                     nullable=False, doc="联系人") 
    
    sign_signature = db.Column(db.String(100), unique=True,
                     nullable=False, doc="租户签名")
    sign_contact = db.Column(db.String(100), unique=True,
                     nullable=False, doc="联系人")
    sign_call = db.Column(db.String(100), unique=True,
                     nullable=False, doc="联系电话")
    sign_email = db.Column(db.String(100), unique=True,
                     nullable=False, doc="电子邮箱")
    sign_replydate = db.Column(db.DateTime, nullable=True, doc="活动有效期")
    
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_timestamp = db.Column(
        db.DateTime, nullable=False, onupdate=datetime.now, default=datetime.now)

    def __repr__(self):
        return '<ShopCardModel %r>' % self.name