import { Component , ViewChild } from "@angular/core";
import { LoginanimComponent } from "./loginanim.component";
import { OtpComponent } from "./otp.component";

@Component({
  selector : 'login',
  templateUrl : '../templates/login.component.html'
})

export class LoginComponent{
  @ViewChild(OtpComponent) ngxOtp: OtpComponent;
  @ViewChild(LoginanimComponent) lganim: LoginanimComponent;

  email: string = '';
  phone:BigInteger;

  login()
  {
    console.log("Login Clicked");

    (async () => {
      const rawResponse = await fetch('http://localhost:3333/request_otp/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({"email": this.email , "name" : "Ruchit" , "phone" : this.phone })
      })

      const content = await rawResponse.json();

      if(content.message == "email has been sent")
      {
        alert('Please Check Your Email for OTP')
        this.ngxOtp.showNgxOtpInput = true;
      }

      console.log(content);
    })();

  }

}
