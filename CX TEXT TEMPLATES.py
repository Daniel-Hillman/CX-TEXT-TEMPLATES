import tkinter as tk
from tkinter import messagebox

# Sample category dictionary (replace with your actual `tom_categories`)
tom_categories = {
    "Tom day 1, 1 missed": (
        "We’ve been notified that you have missed a payment on your TOM Life Insurance "
        "and/or Serious Illness Policy for this month.\n\n"
        "Please respond “YES” to this message for us to automatically reattempt your payment in up to 5 working days. "
        "Or, if you’d like to make this payment manually today, please respond with “LINK” and we can send a payment link to your email.\n\n"
        "If payments are a struggle this month, we have options to help! "
        "Please get in touch with us on 0808 175 2244 or reply to this message."
    ),
    "Tom day 1, very first missed": (
        "We’ve been notified that you have missed your first payment on your Tom Life Insurance and/or Serious Illness Policy for this month.\n"
        "Your policy will cancel 30 days from this missed payment, which was on __.\n\n"
        "To keep your policy, please respond “YES” to this message for us to automatically reattempt your payments in up to 5 working days. "
        "Or, if you’d like to make this payment manually today, please respond with “LINK” and we can send a payment link to your email.\n\n"
        "If you need any help, please get in touch with us on 0808 175 2244 to discuss."
    ),
    "Tom day 1, 2 missed": (
        "We’ve been notified that you now have 2 missed payments on your Life Insurance/ and Serious Illness policy.\n\n"
        "If your next payment is missed, you will enter a cancellation phase.\n\n"
        "If you would like me to try and recollect 1 of the payments within the next 5 working days, please respond 'YES' to this message. "
        "Or, we can send you a payment link to make this manually today.\n\n"
        "If payments are a struggle this month, we have options to help! Please get in touch with us on 0808 175 4747 or reply to this message."
    ),
    "Tom day 1, 3 missed": (
        "You’ve missed 3 payments on your Life Insurance / and Serious Illness Policy.\n\n"
        "Your policy will cancel 30 days from this missed payment.\n\n"
        "To save your policy, please make up at least 1 missed payment within 30 days from the missed payment. "
        "Simply respond ‘YES’ and we can retry the payment. Or we can send you a payment link to make this manually today.\n\n"
        "If you would like to make up more than 1 payment, please let us know in your reply.\n\n"
        "If payments are a struggle this month, we have options to help! Please get in touch with us on 0808 175 2244 or reply to this message."
    ),
    "Tom day 1, cancelled policy mid term": (
        "We’re sorry to see you go. This is just confirmation to let you know that we have processed your cancellation.\n\n"
        "As you are outside of your 30-day cooling off period, the policy will still cover you until the end of this cover period on [] "
        "and then your cover will terminate. There will be one further payment taken for this cover period on [].\n\n"
        "If you feel your policy wasn’t quite right, we can help. Give me a call on 0808 175 2244 or respond to this message with a "
        "good time to give you a call, and we can discuss your options."
    ),
    "Tom day 1, cancelled policy cool off": (
        "We’re sorry to see you go. This is just confirmation to let you know your life insurance policy has now been cancelled.\n\n"
        "As you have cancelled in your 30-day cooling off period, any paid premiums will be refunded to your bank account in up to 14 working days.\n\n"
        "If you feel your policy wasn’t quite right, we can help. Give me a call on 0808 175 2244 or respond to this message with a "
        "good time to give you a call, and we can discuss your options."
    ),
    "Tom day 1, cancelled dd 1 missed": (
        "We’ve been notified that you have missed __ payments due to a cancelled direct debit on your TOM Life Insurance and / Serious Illness Policy for this month.\n\n"
        "Please respond “YES” to this message for us to reinstate the direct debit and we will automatically reattempt your payment/s in 5-10 working days.\n"
        "Or, if you’d like to make this payment manually today, please respond with “LINK” and we can send a payment link to your email.\n\n"
        "If payments are a struggle this month, we have options to help! Please get in touch with us on 0808 175 4747 or reply to this message."
    ),
    "Tom day 1, cancelled dd 0 missed": (
        "We've been notified by our finance department that your direct debit has been cancelled on your Life Insurance policy / and Serious Illness cover.\n\n"
        "This will need to be reinstated ready for your payment that is due on ___. Please respond 'YES' so I can get this sorted for you.\n\n"
        "If you have any issues, please contact us on 0808 175 4747.\n\n"
        "Kind regards,"
    ),
    "Tom day 1, cancelled policy": (
        "We've had confirmation of a request to cancel your Life Insurance policy / Serious Illness cover due to (PROVIDE REASON).\n\n"
        "If you are still interested in having some cover, please reply to this message with the best time for a call back so we can help get you and your family protected again. "
        "Or get in touch with us on 0808 175 2244 to resolve this."
    ),
    "Tom day 2": (
        "We’ve sent you a message regarding your (INPUT REASON) on your Life Insurance / Serious Illness cover and we are still yet to hear from you.\n\n"
        "Please respond to this message or give us a call on 0808 175 2244 so we can get your policy back on track."
    ),
    "Tom day 2, cancelled policy": (
        "We’ve sent you a message regarding your cancelled Life Insurance / and Serious Illness cover and we are yet to hear from you.\n\n"
        "Your policy has now cancelled, we can explore options that are more suitable for you.\n"
        "Let’s discuss this further and find a solution that works for you.\n\n"
        "Please respond to this message or give us a call on 0808 175 2244 so we can get your policy back on track."
    ),
    "Tom day 3, date and time": (
        "We’ve been trying to get in contact with you regarding your policy, but I understand life is busy.\n\n"
        "Please tell us the best date and time for a quick phone call, and we will schedule that in.\n\n"
        "If you have questions, please respond to this message or you can reach us directly on 0808 175 2244."
    ),
    "Tom day 5, missed payments": (
        "We still have a notification on our system regarding your (INPUT REASON) on your Life Insurance Policy/and Serious Illness cover.\n\n"
        "We can help resolve this, but we do need to hear back from you.\n\n"
        "If you’d like to discuss your policy please respond to this message, or you can reach us directly on 0808 175 2244."
    ),
    "Tom day 5, next payment cleared": (
        "The payment on your Life Insurance / and Serious Illness policy for (MONTH) failed, however your latest one has been successful.\n\n"
        "You have the option of keeping this as 1/2 arrear(s) on your account. If you’re happy to do this, reply 'LEAVE'. "
        "To pay the outstanding balance, just reply 'PAYMENT LINK'.\n\n"
        "You can keep a max of 2 arrears on your policy, and that balance will be deducted prior to receiving any payout.\n\n"
        "If you have questions please respond to this message, or you can reach us directly on 0808 175 2244."
    ),
}

def convert_to_polly():
    polly_categories = {}
    for key, value in tom_categories.items():
        polly_categories[key.replace("Tom", "Polly")] = value.replace("TOM", "POLLY").replace("Tom", "Polly")
    return polly_categories

# Generate POLLY categories
polly_categories = convert_to_polly()

# Set up the main application window
root = tk.Tk()
root.title("CX Message Template Selector")
root.geometry("650x400")  # Set window size

# Styling: Background and Font
root.config(bg="#FAFAFA")  # Light grey-white background
font_style = ("Arial", 12)

# Function to copy the TOM message to clipboard
def copy_tom_message():
    selected_template = tom_template_var.get()
    message = tom_categories.get(selected_template, "No message selected")
    root.clipboard_clear()
    root.clipboard_append(message)
    root.update()

# Function to copy the POLLY message to clipboard
def copy_polly_message():
    selected_template = polly_template_var.get()
    message = polly_categories.get(selected_template, "No message selected")
    root.clipboard_clear()
    root.clipboard_append(message)
    root.update()

# Create dropdown list for TOM templates
tom_template_var = tk.StringVar()
tom_template_var.set(list(tom_categories.keys())[0])  # Set default value

tom_template_menu = tk.OptionMenu(root, tom_template_var, *tom_categories.keys())
tom_template_menu.config(font=font_style)
tk.Label(root, text="Select a TOM template:", bg="#FAFAFA", font=font_style).pack(pady=5)
tom_template_menu.pack(pady=5)

# Create dropdown list for POLLY templates
polly_template_var = tk.StringVar()
polly_template_var.set(list(polly_categories.keys())[0])  # Set default value

polly_template_menu = tk.OptionMenu(root, polly_template_var, *polly_categories.keys())
polly_template_menu.config(font=font_style)
tk.Label(root, text="Select a POLLY template:", bg="#FAFAFA", font=font_style).pack(pady=5)
polly_template_menu.pack(pady=5)

# Create buttons to copy TOM and POLLY messages
tom_button = tk.Button(root, text="Copy TOM Message", command=copy_tom_message, bg="#4CAF50", fg="white", font=font_style)
polly_button = tk.Button(root, text="Copy POLLY Message", command=copy_polly_message, bg="#2196F3", fg="white", font=font_style)

# Add buttons to the window
tom_button.pack(pady=10)
polly_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()