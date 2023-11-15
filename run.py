from openAi.completions import run_get_completion
from openAi.prompt_template import run_prompt_template

from openAi.Memory.conversation_buffer import conversationBufferMemory, conversationBufferWindowMemory
from openAi.Memory.conversation_summary import conversationSummaryMemory


doc_string = """Flow \
    Mandate Creation \
    Separate from debit trigger \
    We won't be hitting debit on the day of mandate creation, becoz \
    Retailer will already have a cheque written for distributor \
    It will take 2 business days to create mandate and get it in Reg_success state \
    Mandate creation failed \
    We will communicate this to \
    In such case, a new mandate will have to be created next time from retailer \
    Debit schedule \
    Once a mandate is created, 1 more payment method will pop on app for digital cheque \
    After selecting this, retailer will be prompted to enter cheque date on whatsapp \
    On this day, the debit will be triggered for this mandate \
    Debit trigger \
    Job picks gatewayOrders that need to be debited everyday \
    If a debit fails, it fails, no need to re-trigger.  \
"""
# Basic Completion, send a prompt, get a response
# run_get_completion()

# Template messages
# Can be used for
# Output Parser
# Use a more machine readable formats
# Like JSON, Enums, List, etc
# run_prompt_template()

# Memory
''' 1. conversation_buffer'''
# conversationBufferMemory()
conversationBufferWindowMemory()

# conversationSummaryMemory()
