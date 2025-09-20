import os
import subprocess
from models import db, Weibo_hot

def fetch_weibo_hot():
    """启动微博爬虫（scrapy）并保存数据到数据库"""
    try:
        # 切换到微博爬虫目录
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        weibo_spider_dir = os.path.join(os.path.dirname(__file__), "weibo_hot")

        # 清空之前的微博数据
        Weibo_hot.query.delete()

        # 启动scrapy爬虫
        os.chdir(weibo_spider_dir)
        result = subprocess.run(
            ["scrapy", "crawl", "weibo"],
            capture_output=True,
            text=True,
            timeout=60  # 超时时间
        )

        # 回到项目根目录
        os.chdir(base_dir)

        if result.returncode == 0:
            print("微博爬虫执行成功")
            weibo_hot_list = Weibo_hot.query.all()
            return weibo_hot_list
        else:
            print(f"微博爬虫执行失败：{result.stderr}")
            return []
        
    except Exception as e:
        print("微博爬虫出错：", e)
        # 确保回到原目录
        try:
            os.chdir(base_dir)
        except:
            pass
        return []


if __name__ == "__main__":
    weibo_spider_dir = os.path.join(os.path.dirname(__file__), "weibo_hot")
    print(os.chdir(weibo_spider_dir))