import gradio as gr  # 导入gradio库用于创建GUI

from config import Config  # 导入配置管理模块
from github_client import GitHubClient  # 导入用于GitHub API操作的客户端
from report_generator import ReportGenerator  # 导入报告生成器模块
from llm import LLM  # 导入可能用于处理语言模型的LLM类
from subscription_manager import SubscriptionManager  # 导入订阅管理器
from logger import LOG  # 导入日志记录器

# 创建各个组件的实例
config = Config()
github_client = GitHubClient(config.github_token)
llm = LLM()
report_generator = ReportGenerator(llm)
subscription_manager = SubscriptionManager(config.subscriptions_file)

def export_progress_by_date_range(repo, days):
    # 定义一个函数，用于导出和生成指定时间范围内项目的进展报告

    raw_file_path = github_client.export_progress_by_date_range(repo, days)
    # 导出原始数据文件路径

    report, report_file_path = report_generator.generate_report_by_date_range(
        raw_file_path, days
    )
    # 生成并获取报告内容及文件路径

    return report, report_file_path
    # 返回报告内容和报告文件路径


# 使用 Blocks 创建更加灵活的布局
with gr.Blocks(title="GitHubSentinel") as demo:

    gr.Markdown("# GitHubSentinel 项目进展报告生成器")
    # 页面标题

    # 创建左右结构布局
    with gr.Row():

        # 左侧输入区域
        with gr.Column(scale=5, elem_classes="left-column"):
            with gr.Group():
                repo_dropdown = gr.Dropdown(
                    subscription_manager.list_subscriptions(),
                    label="订阅列表",
                    info="已订阅GitHub项目"
                )
                # 下拉菜单选择订阅的GitHub项目

                days_slider = gr.Slider(
                    value=2,
                    minimum=1,
                    maximum=7,
                    step=1,
                    label="报告周期",
                    info="生成项目过去一段时间进展，单位：天"
                )
                # 滑动条选择报告的时间范围

                with gr.Row():
                    generate_button = gr.Button("生成报告", elem_id="generate_btn")
            # 点击按钮触发报告生成

        # 右侧输出区域
        with gr.Column(scale=6, elem_classes="right-column"):

            gr.Markdown("## 报告预览")
            # 报告预览标题

            report_output = gr.Markdown(
                label="Markdown预览",
                elem_id="report_box"
            )
            # 输出Markdown文本内容

            file_output = gr.File(label="下载报告", elem_id="file_output")
            # 提供报告文件下载，单行显示

    # 按钮点击事件绑定
    generate_button.click(
        fn=export_progress_by_date_range,
        inputs=[repo_dropdown, days_slider],
        outputs=[report_output, file_output]
    )

# 添加滑块进度条动态效果
js_code = """
function updateSliderProgress() {
    // 强制移除所有可能的橙色背景
    const style = document.createElement('style');
    style.textContent = `
        input[type=range].gr-slider,
        input[type=range].slider,
        input[type=range] {
            background: linear-gradient(to right, #238636 0%, #238636 var(--value, 0%), #000000 var(--value, 0%), #000000 100%) !important;
        }
        input[type=range]::-webkit-slider-runnable-track {
            background: transparent !important;
        }
        div:has(> input[type=range]) {
            background: transparent !important;
        }
    `;
    document.head.appendChild(style);

    // 获取所有滑块元素
    const sliders = document.querySelectorAll('input[type="range"]');

    sliders.forEach(slider => {
        // 初始化进度
        function setProgress() {
            const min = parseFloat(slider.min) || 1;
            const max = parseFloat(slider.max) || 7;
            const val = parseFloat(slider.value) || 2;
            const percentage = ((val - min) / (max - min)) * 100;

            // 设置CSS变量
            slider.style.setProperty('--value', percentage + '%', 'important');

            // 直接设置background，确保覆盖
            slider.style.background = `linear-gradient(to right, #238636 0%, #238636 ${percentage}%, #000000 ${percentage}%, #000000 100%)`;
        }

        // 设置初始进度
        setProgress();

        // 监听滑块变化事件
        slider.addEventListener('input', function() {
            setProgress();
        });

        // 监听鼠标松开事件，确保最终位置正确
        slider.addEventListener('change', function() {
            setProgress();
        });
    });
}

// 在多个时间点执行，确保覆盖
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateSliderProgress);
} else {
    updateSliderProgress();
}

// 监听 Gradio 更新事件
document.addEventListener('gradio:connected', function() {
    setTimeout(updateSliderProgress, 100);
    setTimeout(updateSliderProgress, 500);
});

// 每隔一段时间检查一次，确保滑块样式更新
setInterval(updateSliderProgress, 200);
"""

css_code = """
    body {
        background-color: #0d1117;
    }

    /* 右侧 Markdown 报告容器，高度固定，宽度自适应 */
    #report_box {
        height: 350px;      
        overflow-y: auto;   
        padding: 24px;
        border-radius: 8px;
        background-color: #161b22;   
        border: 1px solid #30363d;   
        color: #c9d1d9;              
        font-size: 14px;
        line-height: 1.6;
        width: 100%;                 
    }

    /* 标题风格 */
    #report_box h1 {
        font-size: 22px;
        border-bottom: 1px solid #30363d;
        padding-bottom: 8px;
    }
    #report_box h2 {
        font-size: 18px;
        margin-top: 24px;
    }
    #report_box h3 {
        font-size: 16px;
        margin-top: 16px;
    }

    /* 链接 */
    #report_box a {
        color: #58a6ff;
        text-decoration: none;
    }
    #report_box a:hover {
        text-decoration: underline;
    }

    /* 代码块 */
    #report_box pre {
        background-color: #0d1117 !important;
        border: 1px solid #30363d;
        padding: 12px;
        border-radius: 6px;
    }
    #report_box code {
        background-color: #21262d;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 13px;
    }

    /* 列表间距 */
    #report_box ul {
        padding-left: 20px;
    }

    /* 滚动条 */
    #report_box::-webkit-scrollbar {
        width: 8px;
    }
    #report_box::-webkit-scrollbar-thumb {
        background: #30363d;
        border-radius: 4px;
    }

    /* GitHub 风格主按钮 */
    #generate_btn {
        background-color: #238636;     
        border: 1px solid #2ea043;
        color: white;
        padding: 8px 16px;
        border-radius: 6px;
        font-weight: 500;
        font-size: 14px;
        width: auto !important;        
        min-width: 120px;
    }
    #generate_btn:hover {
        background-color: #2ea043;
    }

    /* 中间间距 */
    #gr-row {
        gap: 32px !important;   
    }

    /* 左侧 Column 最小宽度 */
    .left-column {
        min-width: 300px;
    }

    /* 下载文件框紧凑，不占用整列高度 */
    #file_output {
        height: 80px;
        margin-top: 8px;        
        display: block;          
    }

    /* ===================== Slider 样式 ===================== */
    /* 滑块容器 - 强制覆盖所有样式 */
    input[type=range].gr-slider, 
    input[type=range].slider,
    input[type=range] {
        -webkit-appearance: none !important;
        appearance: none !important;
        background: linear-gradient(to right, #238636 0%, #238636 var(--value, 0%), #000000 var(--value, 0%), #000000 100%) !important;
        background-color: transparent !important;
        height: 6px !important;
        border-radius: 3px !important;
        outline: none !important;
        padding: 0 !important;
        margin: 10px 0 !important;
        box-shadow: none !important;
        border: none !important;
        width: 100% !important;
    }

    /* 移除轨道默认背景 */
    input[type=range]::-webkit-slider-runnable-track {
        background: transparent !important;
        border: none !important;
        height: 6px !important;
    }

    input[type=range]::-moz-range-track {
        background: transparent !important;
        border: none !important;
        height: 6px !important;
    }

    input[type=range]::-ms-track {
        background: transparent !important;
        border: none !important;
        height: 6px !important;
        color: transparent !important;
    }

    /* 滑块 - 圈圈 */
    input[type=range]::-webkit-slider-thumb {
        -webkit-appearance: none !important;
        appearance: none !important;
        width: 18px !important;
        height: 18px !important;
        background: #238636 !important;
        border: 2px solid #2ea043 !important;
        border-radius: 50% !important;
        cursor: pointer !important;
        margin-top: -6px !important;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.3) !important;
        z-index: 2 !important;
        position: relative !important;
    }

    input[type=range]::-moz-range-thumb {
        width: 18px !important;
        height: 18px !important;
        background: #238636 !important;
        border: 2px solid #2ea043 !important;
        border-radius: 50% !important;
        cursor: pointer !important;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.3) !important;
        z-index: 2 !important;
        position: relative !important;
    }

    input[type=range]::-ms-thumb {
        width: 18px !important;
        height: 18px !important;
        background: #238636 !important;
        border: 2px solid #2ea043 !important;
        border-radius: 50% !important;
        cursor: pointer !important;
        margin-top: 0 !important;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.3) !important;
        z-index: 2 !important;
        position: relative !important;
    }

    /* Firefox 进度条颜色 */
    input[type=range]::-moz-range-progress {
        height: 6px !important;
        background: #238636 !important;
        border-radius: 3px 0 0 3px !important;
    }

    /* Edge/IE 进度条颜色 */
    input[type=range]::-ms-fill-lower {
        background: #238636 !important;
        border-radius: 3px !important;
    }

    input[type=range]::-ms-fill-upper {
        background: #000000 !important;
        border-radius: 3px !important;
    }

    /* 移除任何可能的橙色伪元素或背景 */
    input[type=range]::before,
    input[type=range]::after,
    input[type=range] *::before,
    input[type=range] *::after {
        background: transparent !important;
        display: none !important;
    }

    /* 强制移除 Gradio 的默认容器样式 */
    div:has(> input[type=range]) {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    .slider-container, 
    .slider-outer,
    .slider-inner {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }
"""
# 启动界面，本地访问，不需要公网
demo.launch(
    server_name="0.0.0.0",
    server_port=7860,
    js=js_code,
    css=css_code
)