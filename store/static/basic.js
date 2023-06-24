var $j = jQuery.noConflict();
$j(document).ready(function () {
  $('[data-toggle="popover"]').popover();
});

$("#popoverCart").popover({ html: true, sanitize: false });
function updatePopover(cart) {
  var popStr = "";
  popStr = popStr + "<div>";
  for (var item in cart) {
    a = item.slice(2);
    if (cart[item][0] != 0) {
      popStr += cart[item][1] + " Qty:" + cart[item][0] + "<br>";
    }
  }
  popStr +=
    "<hr></div> <a href='/store/checkout'><button class='btn btn-primary' id='checkout'>Checkout</button></a> <br><button class='btn btn-primary' id='clearCart' style='margin-top:6px' onclick='clearCart()'>Clear Cart</button>";

  document.getElementById("popoverCart").setAttribute("data-content", popStr);
}
// function updateCart(cart) {
//   for (var item in cart) {
//     document.getElementById("div" + item).innerHTML =
//       "<button id= 'minus" +
//       item +
//       "' class='btn btn-primary minus' style='margin-bottom: 10px'>-</button> <span id='val" +
//       item +
//       "'' style='margin-bottom: 10px'>" +
//       cart[item][0] +
//       "</span> <button id='plus" +
//       item +
//       "' class='btn btn-primary plus' style='margin-bottom: 10px'>+ </button>";
//   }
//   localStorage.setItem("cart", JSON.stringify(cart));
//   var sum = 0;
//   for (var item in cart) {
//     // console.log(item);
//     sum += cart[item][0];
//   }
//   document.getElementById("navCart").innerHTML = sum;
// }
// function clearCart() {
//   cart = JSON.parse(localStorage.getItem("cart"));
//   for (var item in cart) {
//     document.getElementById("div" + item).innerHTML =
//       '<button id="' +
//       item +
//       '"class="btn btn-primary plus" style="margin-bottom: 10px">Add to Cart</button>';
//   }
//   localStorage.clear();
//   cart = {};
//   updateCart(cart);
// }

if (localStorage.getItem("cart") == null) {
  var cart = {};
} else {
  cart = JSON.parse(localStorage.getItem("cart"));
  var sum = 0;
  for (var item in cart) {
    sum += cart[item][0];
  }
  document.getElementById("navCart").innerHTML = sum;
  // updateCart(cart);
  updatePopover(cart);
  $("#popoverCart").popover("hide");
}
// $(document).on("click", ".cart", function () {
// $(".divpr").on("click", "button.cart", function () {
//   var idstr = this.id.toString();
//   if (cart[idstr] != undefined) {
//     qty = cart[idstr][0] + 1;
//     console.log(cart);
//   } else {
//     qty = 1;
//     name = document.getElementById("name" + idstr).innerHTML;
//     cart[idstr] = [qty, name];
//   }
//   // updateCart(cart);
//   updatePopover(cart);
//   $("#popoverCart").popover("hide");
// });
// $(document).on("click", ".divpr button.minus", function () {
//   a = this.id.slice(7);
//   cart["pr" + a][0] = cart["pr" + a][0] - 1;
//   cart["pr" + a][0] = Math.max(0, cart["pr" + a][0]);
//   document.getElementById("valpr" + a).innerHTML = cart["pr" + a][0];
//   updateCart(cart);
//   updatePopover(cart);
//   $("#popoverCart").popover("hide");
// });
// $(document).on("click", ".divpr button.plus", function () {
//   a = this.id.slice(6);
//   cart["pr" + a][0] = cart["pr" + a][0] + 1;
//   document.getElementById("valpr" + a).innerHTML = cart["pr" + a][0];
//   updateCart(cart);
//   updatePopover(cart);
//   $("#popoverCart").popover("hide");
// });
