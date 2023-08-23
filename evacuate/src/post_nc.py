import netCDF4 as nc

__author__ = 'Nan Jia'
__email__ = 'KoiGoko@outlook.com'


def read_nc_file(filename):
    # 打开 NetCDF 文件
    dataset = nc.Dataset(filename, 'r')
    return dataset


if __name__ == "__main__":
    filename = 'res_xr.nc'  # 文件路径
    dataset = read_nc_file(filename)

    # 获取数据变量 'data'
    data_var = dataset.variables['data']

    # 获取维度的长度
    vehicle_length = len(dataset.dimensions['vehicle'])
    value_length = len(dataset.dimensions['value'])

    # 读取每一层并打印
    for layer_idx in range(vehicle_length):
        layer = data_var[:, :, 564:569]
        print(layer.shape)
        print(f"Layer {layer_idx + 1}:")
        print(layer)

    # 关闭数据集
    dataset.close()
