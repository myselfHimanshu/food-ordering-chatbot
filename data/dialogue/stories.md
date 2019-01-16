## story 01
* greetings.hello
- utter_greetings.hello
- utter_agent.welcome
- utter_ask.cuisine

## story 02
* cuisine.type
- utter_display.menu
- utter_select.item
- utter_item.not_available


## story 03
* cuisine.type
- utter_display.menu
- utter_select.item
- utter_item.quantity.how_many
- utter_order.confirm


## story 04
* cuisine.type
- utter_display.menu
- utter_select.item
- utter_item.quantity.how_many
- utter_order.confirm
* confirm.affirm
- utter_order.placed

## story 05
* cuisine.type
- utter_display.menu
- utter_select.item
- utter_item.quantity.how_many
- utter_order.confirm
* confirm.deny
- utter_order.anything_else
* confirm.deny
- utter_greetings.bye

## story 06
* cuisine.type
- utter_display.menu
- utter_select.item
- utter_item.quantity.how_many
- utter_order.confirm
* confirm.deny
- utter_order.anything_else
* confirm.affirm
- utter_ask.cuisine

## story 07
* cuisine.type
- utter_display.menu
- utter_select.item
- utter_item.not_available
- utter_order.anything_else
* confirm.affirm
- utter_ask.cuisine

## story 08
* cuisine.type
- utter_display.menu
- utter_select.item
- utter_item.not_available
- utter_order.anything_else
* confirm.deny
- utter_greetings.bye


##Bye
* greetings.bye
- utter_greetings.bye


## Generated Story -7329490837376575624
* greetings.hello
    - utter_greetings.hello
    - utter_agent.welcome
    - utter_ask.cuisine
* cuisine.type{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_display.menu
    - utter_select.item
* selected.item{"food": "burger"}
    - utter_item.quantity.how_many
* item.quantity{"quant": "5"}
    - utter_order.confirm
* confirm.affirm
    - utter_order.placed
* greetings.bye
    - utter_greetings.bye
## Generated Story 5839383529639089139
* greetings.hello
    - utter_greetings.hello
    - utter_agent.welcome
    - utter_ask.cuisine
* cuisine.type{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_display.menu
    - utter_select.item
* cuisine.type{"food": "idli sambar"}
    - utter_item.not_available
    - utter_select.item
* selected.item{"food": "chawal"}
    - utter_item.quantity.how_many
* item.quantity{"quant": "1"}
    - utter_order.confirm
* confirm.affirm
    - utter_order.placed
    - utter_order.anything_else
* confirm.deny
    - utter_greetings.bye
* greetings.bye
## Generated Story 642101536649265633
* greetings.hello
    - utter_agent.welcome
    - utter_ask.cuisine
* selected.item{"food": "biryani"}
    - utter_item.not_available
* confirm.affirm
    - utter_ask.cuisine
* cuisine.type{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_display.menu
    - utter_select.item
* selected.item{"food": "chole"}
    - utter_item.quantity.how_many
* item.quantity{"quant": "2"}
    - utter_order.confirm
* confirm.affirm
    - utter_order.placed
    - utter_order.anything_else
* confirm.deny
    - utter_greetings.bye
* greetings.bye
## Generated Story -808200451385065654
* greetings.hello
    - utter_agent.welcome
    - utter_ask.cuisine
* cuisine.type{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_display.menu
    - utter_select.item
* selected.item{"food": "noodles"}
    - utter_item.not_available
* confirm.affirm
    - utter_select.item
* item.quantity
    - utter_order.anything_else
* confirm.deny
    - utter_order.confirm
* confirm.affirm
    - utter_order.placed
* greetings.bye
    - utter_greetings.bye

## Generated Story -2265131988202812861
* greetings.hello
    - utter_agent.welcome
    - utter_ask.cuisine
* cuisine.type{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_display.menu
    - utter_select.item
* selected.item{"food": "paratha"}
    - utter_order.anything_else
* confirm.affirm
    - utter_select.item
* selected.item{"food": "burger"}
    - utter_item.quantity.how_many
* item.quantity{"quant": "4"}
    - utter_order.anything_else
* confirm.deny
    - utter_order.confirm
* confirm.affirm
    - utter_order.placed
* greetings.bye
    - utter_greetings.bye

## Generated Story 7806388375038758874
* greetings.hello
    - utter_agent.welcome
    - utter_ask.cuisine
* cuisine.type{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_display.menu
    - utter_select.item
* confirm.deny
    - utter_greetings.bye

