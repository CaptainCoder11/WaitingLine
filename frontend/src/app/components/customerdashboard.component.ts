import { Component , Inject,Input, ViewChild } from "@angular/core";
import { parseJSON } from "cypress/types/jquery";
import { CookieService } from "ngx-cookie-service";
import { LoginanimComponent } from "./loginanim.component";
import { WaitinganimComponent } from "./waitanim.component";

@Component({
  selector : 'stores',
  templateUrl : '../templates/customerdashboard.component.html'
})
export class CustomerDashboardComponent{
  @ViewChild(WaitinganimComponent) lganim: LoginanimComponent;
  constructor(private cookieService: CookieService) { }

  logo:any
  ngOnInit(): void {
    this.logo = this.cookieService.get('logo');

    console.log(this.cookieService.get('logo'));


    (async () => {
      const rawResponse = await fetch('http://localhost:3333/get_appointments', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          "store_id": this.cookieService.get('storeid')
        })

    })
      const content = await rawResponse.json();
      console.log(content)

      for(let c of content)
      {
        var d = c.time_of_arrival
        var t = new Date(d)
        var hr = ("0" + t.getHours()).slice(-2);
        var min = ("0" + t.getMinutes()).slice(-2);
        console.log(hr + "::"+min);
      }




    })();


  }

}
