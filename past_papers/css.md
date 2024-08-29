### CSS Cheat Sheet

#### **Colors**
- **Background Color:** `background-color: color;`
- **Text Color:** `color: color;`
- **Border Color:** `border-color: color;`

#### **Text Styling**
- **Font Size:** `font-size: size;`
- **Font Family:** `font-family: 'font-name', fallback;`
- **Font Weight:** `font-weight: normal | bold | number;`
- **Text Alignment:** `text-align: left | center | right | justify;`
- **Text Decoration:** `text-decoration: none | underline | line-through;`
- **Text Transform:** `text-transform: uppercase | lowercase | capitalize;`

#### **Background**
- **Background Color:** `background-color: color;`
- **Background Image:** `background-image: url('image.jpg');`
- **Background Position:** `background-position: top | center | bottom | left | right;`
- **Background Size:** `background-size: auto | cover | contain;`
- **Background Repeat:** `background-repeat: repeat | no-repeat;`

#### **Borders**
- **Border Style:** `border-style: none | solid | dashed | dotted;`
- **Border Width:** `border-width: width;`
- **Border Color:** `border-color: color;`
- **Border Radius:** `border-radius: radius;` (e.g., `5px` for rounded corners)

#### **Box Model**
- **Padding:** `padding: top right bottom left;` (e.g., `10px 20px 10px 20px` or `10px` for all sides)
- **Margin:** `margin: top right bottom left;` (e.g., `10px 20px 10px 20px` or `10px` for all sides)
- **Width:** `width: value;` (e.g., `100px`, `50%`)
- **Height:** `height: value;` (e.g., `100px`, `auto`)

#### **Display and Positioning**
- **Display:** `display: block | inline | inline-block | none;`
- **Position:** `position: static | relative | absolute | fixed | sticky;`
- **Top/Right/Bottom/Left:** `top: value;`, `right: value;`, `bottom: value;`, `left: value;`
- **Z-Index:** `z-index: value;`

#### **Buttons**
- **Background Color:** `background-color: color;`
- **Text Color:** `color: color;`
- **Border:** `border: width style color;`
- **Padding:** `padding: top right bottom left;`
- **Font Size:** `font-size: size;`
- **Border Radius:** `border-radius: radius;`
- **Cursor:** `cursor: pointer;` (changes cursor to a hand on hover)
- **Hover Effects:** `button:hover { property: value; }`

#### **Flexbox**
- **Display Flex:** `display: flex;`
- **Flex Direction:** `flex-direction: row | column;`
- **Justify Content:** `justify-content: flex-start | center | space-between | space-around;`
- **Align Items:** `align-items: flex-start | center | flex-end | stretch;`
- **Align Self:** `align-self: auto | flex-start | center | flex-end | stretch;`

#### **Grid**
- **Display Grid:** `display: grid;`
- **Grid Template Columns:** `grid-template-columns: value;` (e.g., `1fr 2fr`)
- **Grid Template Rows:** `grid-template-rows: value;`
- **Grid Column:** `grid-column: start / end;`
- **Grid Row:** `grid-row: start / end;`

#### **Transitions and Animations**
- **Transition:** `transition: property duration timing-function delay;`
- **Animation:** `animation: name duration timing-function delay iteration-count direction;`

### Examples

1. **Button with Background Color and Padding:**
   ```css
   button {
       background-color: blue;
       color: white;
       padding: 10px 20px;
       border: none;
       border-radius: 5px;
       cursor: pointer;
   }
   ```

2. **Text Centering and Font Styling:**
   ```css
   p {
       text-align: center;
       font-size: 18px;
       color: darkgray;
   }
   ```

3. **Flexbox Container:**
   ```css
   .container {
       display: flex;
       justify-content: center;
       align-items: center;
       height: 100vh;
   }
   ```

This cheat sheet should help you choose the right CSS properties for various styling needs. Feel free to adapt and expand it based on your specific design requirements!
