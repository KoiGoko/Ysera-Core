import evacuate.src.pre_private as private
import evacuate.src.pre_public as public
import evacuate.src.change_sumocfg as change_sumocfg
from evacuate.src.global_init import global_init

__author__ = 'Nan Jia'
__email__ = 'KoiGoko@outlook.com'

if __name__ == '__main__':
    # 配置参数路径
    cfg_path = r'D:\Ysera\Ysera-Core\evacuate\cfg'
    # 模拟文件路径
    xml_path = r'D:\Ysera\Ysera-Core\evacuate\xiapu\xiapu'

    # 初始化全局配置
    global_init(cfg_path)

    # 私家车配置初始化
    private.private_run(cfg_path, xml_path)

    # 初始化公共车辆调度
    public.public_run(cfg_path, xml_path)

    # 初始化sumocfg文件
    change_sumocfg.init_sumocfg(xml_path)
