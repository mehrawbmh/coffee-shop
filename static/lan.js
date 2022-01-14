$(document).ready(function () {
  let switcher = $(".switcher");
  let signup_section = $(".English");
  let signin_section = $(".فارسی");
  switcher.click(function () {
    let value = switcher.html();
    if (value == "فارسی") {
      signup_section.fadeOut();
      signin_section.fadeIn();
      switcher.html("Enghlish");
    } else {
      // is Sign Up
      signin_section.fadeOut();
      signup_section.fadeIn();
      switcher.html("فارسی");
    }
  });
});
