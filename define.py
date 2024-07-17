from typing import List, Any, Optional


class AccountGetter:



    def __init__(self):
        return






class Account:
    def __init__(self, is_show_alipay_privilege, equip_desc, create_time_desc, has_trade_history, is_seller,
                 allow_taken_time, is_equip_trying, appointed_roleid, server_name, has_sim_trade_history,
                 highlights, kindid, area_name, support_video_preview, alipay_info, equip_locked,
                 search_type, equip_count, equip_name, is_set_general, selling_time, status,
                 offsale_then_take_back, support_3d_preview, can_bid_random_draw, create_time,
                 equipid, buyer_fee_list, fair_show_end_time, allow_bargain, min_buy_level,
                 equip_detail_url, allow_fair_show_buy, equip_lock_time_desc, fair_show_poundage_origin,
                 desc_sumup_short, cross_buy_serverid_list, is_support_kol, equip_onsale_version,
                 diy_desc, random_draw_finish_time, coupon_data, allow_cross_buy, block_diy_description,
                 tranx_goods_sn, joined_seller_activity, fair_show_poundage_desc, storage_type,
                 is_show_special_highlight, collect_num, appointed_data, level_desc,
                 selling_time_ago_desc, is_support_instalment, allow_urs_bargain, allow_appoint,
                 equip_type_inspection_view_url, expire_remain_seconds, show_open_bargain_button,
                 show_transfer_to_combat_area_tips, pass_fair_show, is_random_draw_period, game_ordersn,
                 price_explanation, platform_type, eid, equip_server_sn, is_equip_can_try,
                 allow_multi_order, poundage_list, equip_level, is_weijianding, product, equip_type,
                 price, other_info, status_desc, equip_type_desc, unpaid_user_order, expire_time,
                 serverid, is_my_equip, icon, fair_show_poundage, is_owner, complex_highlights_v2,
                 game_compete_serverid, activity_info, open_fair_show_end_notice, game_channel):
        self.is_show_alipay_privilege = is_show_alipay_privilege  # 是否显示支付宝特权
        self.equip_desc = equip_desc
        self.create_time_desc = create_time_desc  # 创建时间描述
        self.has_trade_history = has_trade_history  # 是否有交易历史
        self.is_seller = is_seller  # 是否为卖家
        self.allow_taken_time = allow_taken_time  # 允许的时间戳
        self.is_equip_trying = is_equip_trying  # 是否正在试装备
        self.appointed_roleid = appointed_roleid  # 指定角色ID
        self.server_name = server_name  # 服务器名称
        self.has_sim_trade_history = has_sim_trade_history  # 是否有类似交易历史
        self.highlights = highlights  # 亮点信息
        self.kindid = kindid  # 类型ID
        self.area_name = area_name  # 区域名称
        self.support_video_preview = support_video_preview  # 是否支持视频预览
        self.alipay_info = alipay_info  # 支付宝信息
        self.equip_locked = equip_locked  # 装备是否锁定
        self.search_type = search_type  # 搜索类型
        self.equip_count = equip_count  # 装备数量
        self.equip_name = equip_name  # 装备名称
        self.is_set_general = is_set_general  # 是否设置为将军
        self.selling_time = selling_time  # 销售时间
        self.status = status  # 状态
        self.offsale_then_take_back = offsale_then_take_back  # 下架后是否撤回
        self.support_3d_preview = support_3d_preview  # 是否支持3D预览
        self.can_bid_random_draw = can_bid_random_draw  # 是否可以随机抽奖
        self.create_time = create_time  # 创建时间
        self.equipid = equipid  # 装备ID
        self.buyer_fee_list = buyer_fee_list  # 买家费用列表
        self.fair_show_end_time = fair_show_end_time  # 公平展示结束时间
        self.allow_bargain = allow_bargain  # 是否允许还价
        self.min_buy_level = min_buy_level  # 最低购买等级
        self.equip_detail_url = equip_detail_url  # 装备详情链接
        self.allow_fair_show_buy = allow_fair_show_buy  # 是否允许公平展示购买
        self.equip_lock_time_desc = equip_lock_time_desc  # 装备锁定时间描述
        self.fair_show_poundage_origin = fair_show_poundage_origin  # 公平展示手续费
        self.desc_sumup_short = desc_sumup_short  # 简短描述总结
        self.cross_buy_serverid_list = cross_buy_serverid_list  # 跨服购买服务器ID列表
        self.is_support_kol = is_support_kol  # 是否支持KOL
        self.equip_onsale_version = equip_onsale_version  # 装备上架版本
        self.diy_desc = diy_desc  # DIY描述
        self.random_draw_finish_time = random_draw_finish_time  # 随机抽奖完成时间
        self.coupon_data = coupon_data  # 优惠券数据
        self.allow_cross_buy = allow_cross_buy  # 是否允许跨服购买
        self.block_diy_description = block_diy_description  # 是否阻止DIY描述
        self.tranx_goods_sn = tranx_goods_sn  # 交易商品编号
        self.joined_seller_activity = joined_seller_activity  # 是否参与卖家活动
        self.fair_show_poundage_desc = fair_show_poundage_desc  # 公平展示手续费描述
        self.storage_type = storage_type  # 存储类型
        self.is_show_special_highlight = is_show_special_highlight  # 是否显示特殊亮点
        self.collect_num = collect_num  # 收藏数量
        self.appointed_data = appointed_data  # 指定数据
        self.level_desc = level_desc  # 等级描述
        self.selling_time_ago_desc = selling_time_ago_desc  # 销售时间描述
        self.is_support_instalment = is_support_instalment  # 是否支持分期付款
        self.allow_urs_bargain = allow_urs_bargain  # 是否允许URS还价
        self.allow_appoint = allow_appoint  # 是否允许预约
        self.equip_type_inspection_view_url = equip_type_inspection_view_url  # 装备类型检查视图链接
        self.expire_remain_seconds = expire_remain_seconds  # 剩余过期时间（秒）
        self.show_open_bargain_button = show_open_bargain_button  # 是否显示打开还价按钮
        self.show_transfer_to_combat_area_tips = show_transfer_to_combat_area_tips  # 是否显示转移到战斗区提示
        self.pass_fair_show = pass_fair_show  # 是否通过公平展示
        self.is_random_draw_period = is_random_draw_period  # 是否为随机抽奖期
        self.game_ordersn = game_ordersn  # 游戏订单编号
        self.price_explanation = price_explanation  # 价格说明
        self.platform_type = platform_type  # 平台类型
        self.eid = eid  # 事件ID
        self.equip_server_sn = equip_server_sn  # 装备服务器编号
        self.is_equip_can_try = is_equip_can_try  # 装备是否可以试用
        self.allow_multi_order = allow_multi_order  # 是否允许多订单
        self.poundage_list = poundage_list  # 手续费列表
        self.equip_level = equip_level  # 装备等级
        self.is_weijianding = is_weijianding  # 是否为未鉴定
        self.product = product  # 产品
        self.equip_type = equip_type  # 装备类型
        self.price = price  # 价格
        self.other_info = other_info  # 其他信息
        self.status_desc = status_desc  # 状态描述
        self.equip_type_desc = equip_type_desc  # 装备类型描述
        self.unpaid_user_order = unpaid_user_order  # 未支付用户订单
        self.expire_time = expire_time  # 过期时间
        self.serverid = serverid  # 服务器ID
        self.is_my_equip = is_my_equip  # 是否为我的装备
        self.icon = icon  # 图标
        self.fair_show_poundage = fair_show_poundage  # 公平展示手续费
        self.is_owner = is_owner  # 是否为拥有者
        self.complex_highlights_v2 = complex_highlights_v2  # 复杂亮点V2
        self.game_compete_serverid = game_compete_serverid  # 游戏竞争服务器ID
        self.activity_info = activity_info  # 活动信息
        self.open_fair_show_end_notice = open_fair_show_end_notice  # 是否打开公平展示结束通知
        self.game_channel = game_channel  # 游戏渠道

    def __repr__(self):
        return f"<Account(name={self.server_name}, status={self.status_desc})>"

# 定义表示装备信息的 Gear 类
class Gear:
    def __init__(self, advance: int, next_trade_time: int, name: str, level: int, equip_condition: List[str],
                 is_defective: int, feature: List[Any], feature_id: int, gear_id: int, show_gear_id: int,
                 skillInfo: List[List[Any]], phase: int, heroId: int, level_type: int, is_bind: int, is_confirm: int):
        self.advance = advance  # 装备的进阶等级
        self.next_trade_time = next_trade_time  # 下次交易时间
        self.name = name  # 装备名称
        self.level = level  # 装备等级
        self.equip_condition = equip_condition  # 装备条件
        self.is_defective = is_defective  # 是否为残次品
        self.feature = feature  # 装备特性
        self.feature_id = feature_id  # 特性ID
        self.gear_id = gear_id  # 装备ID
        self.show_gear_id = show_gear_id  # 展示的装备ID
        self.skillInfo = skillInfo  # 技能信息
        self.phase = phase  # 阶段
        self.heroId = heroId  # 英雄ID
        self.level_type = level_type  # 等级类型
        self.is_bind = is_bind  # 是否绑定
        self.is_confirm = is_confirm  # 是否确认


class Hero:
    country_list = ['汉', '魏', '蜀', '吴', '群', '晋']
    hero_type_advance_list = {'12': '重步兵', '22': '长枪兵', '13': '重骑兵',
                              '23': '轻骑兵', '43': '铁骑兵', '11': '长弓兵',
                              '21': '弩兵', '32': '禁卫', '31': '死士',
                              '52': '蛮兵'}
    hero_type_list = ['弓兵', '步兵', '骑兵']





    def __init__(self, hit_range: int, hero_type_advance: int, dynamic_icon: int, card_border: str, hero_type: int,
                 is_support: bool, cost: float, quality: int, awake_state: int, is_season_card: int, hero_id: int,
                 gear: Optional[Gear], season: str, advance_num: int, policy_awake_state: int, name: str,
                 army_facade: List[Any], country: int, cfg_hero_type_availible: List[int], hero_type_availible: List[int],
                 icon_hero_id: int, hero_features: int):
        self.hit_range = hit_range  # 攻击范围
        self.hero_type_advance = hero_type_advance  # 英雄类型进阶
        self.dynamic_icon = dynamic_icon  # 动态图标
        self.card_border = card_border  # 卡片边框
        self.hero_type = hero_type  # 英雄类型
        self.is_support = is_support  # 是否为支援英雄
        self.cost = cost  # 成本
        self.quality = quality  # 品质
        self.awake_state = awake_state  # 觉醒状态
        self.is_season_card = is_season_card  # 是否为季节卡
        self.hero_id = hero_id  # 英雄ID
        self.gear = gear  # 装备信息，允许为 None
        self.season = season  # 季节
        self.advance_num = advance_num  # 进阶次数
        self.policy_awake_state = policy_awake_state  # 策略觉醒状态
        self.name = name  # 英雄名称
        self.army_facade = army_facade  # 军队外观
        self.country = country  # 国家
        self.cfg_hero_type_availible = cfg_hero_type_availible  # 配置的可用英雄类型
        self.hero_type_availible = hero_type_availible  # 可用的英雄类型
        self.icon_hero_id = icon_hero_id  # 图标英雄ID
        self.hero_features = hero_features  # 英雄特性

    def display_info(self):
        info = (
            f"攻击距离: {self.hit_range}\n"
            f"进阶兵种: {self.hero_type_advance}\n"
            f"武将名称: {self.name}\n"
            f"可以转的兵种: {self.cfg_hero_type_availible}\n"
            f"觉醒状态: {self.awake_state}\n"
            f"势力: {self.country_list[int(self.country) - 1]}\n"
            f"卡框: {self.card_border}\n"
            f"赛季卡: {'是' if self.is_season_card else '否'}\n"
            f"红度: {self.advance_num}\n"
            f"已经转的兵种: {self.hero_type_availible}\n"
            f"兵种: {self.hero_type}\n"
            f"动态图标: {self.dynamic_icon}\n"
            f"支援: {'是' if self.is_support else '否'}\n"
            f"花费: {self.cost}\n"
            f"赛季: {self.season}\n"
            f"政策觉醒状态: {self.policy_awake_state}\n"
            f"武将图像ID: {self.icon_hero_id}\n"
            f"武将特征: {self.hero_features}\n"
            f"星级: {self.quality}\n"
            f"军队外观: {self.army_facade}\n"
            f"武将ID: {self.hero_id}\n"
        )
        return info

    def __repr__(self):
        return f"Hero(name={self.name}, hero_id={self.hero_id})"

