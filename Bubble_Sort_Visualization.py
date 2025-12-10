import random
import gradio as gr

MAX_STEPS = 8


def generate_list():
    arr = random.sample(range(1, 101), 5)
    display = f"Random List:\n{arr}"
    return display, arr


def bubble_sort_on_state(arr_state):
    if not arr_state:
        list_msg = "⚠️ Please click 'Generate List' first."
        return (
            list_msg,
            *["" for _ in range(MAX_STEPS)],
            *["" for _ in range(MAX_STEPS)],
            "⚠️ No list to sort."
        )


    arr = arr_state[:]
    steps = []
    ranges = []
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            steps.append(f"Compare {arr[j]} and {arr[j+1]}")
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                steps.append(f"Swap {arr[j+1]} and {arr[j]}")
                swapped = True
            ranges.append(f"Current List: {arr}")
        if not swapped:
            break


    if len(steps) < MAX_STEPS:
        steps.extend(["" for _ in range(MAX_STEPS - len(steps))])
    if len(ranges) < MAX_STEPS:
        ranges.extend(["" for _ in range(MAX_STEPS - len(ranges))])


    final_msg = f"✅ Sorted List: {arr}\nComparisons: {comparisons} | Swaps: {swaps}"
    list_display = f"Random List:\n{arr_state}"


    return list_display, *steps[:MAX_STEPS], *ranges[:MAX_STEPS], final_msg


#UI
with gr.Blocks(title="Bubble Sort Visualization") as demo:
    gr.Markdown(
        """
        # 🎯 Bubble Sort Visualization
        **Step 1:** Click **Generate List** (5 unique numbers in 1–100).  
        **Step 2:** Click **Run Bubble Sort**.  
        See each comparison and swap, and the list state after each pass.
        """
    )

    arr_state = gr.State([])
    with gr.Row():
        gen_btn = gr.Button("Generate List 🎲", variant="secondary")
        run_btn = gr.Button("Run Bubble Sort 🔄", variant="primary")
    list_box = gr.Textbox(label="Generated List", lines=2, interactive=False)
    gr.Markdown("### 🔹 Sort Steps (Comparison and Swap)")


    step_boxes = [gr.Textbox(label=f"Step {i+1}", lines=1, interactive=False) for i in range(MAX_STEPS)]
    gr.Markdown("### 🔸 List State After Each Pass")
    range_boxes = [gr.Textbox(label=f"Pass {i+1}", lines=1, interactive=False) for i in range(MAX_STEPS)]
    result_box = gr.Textbox(label="Final Result", lines=2, interactive=False)


    gen_btn.click(
        fn=generate_list,
        inputs=[],
        outputs=[list_box, arr_state],
    )
    run_btn.click(
        fn=bubble_sort_on_state,
        inputs=[arr_state],
        outputs=[list_box, *step_boxes, *range_boxes, result_box],
    )


if __name__ == "__main__":
    demo.launch(share=True)