import { Component , Inject,Input, ViewChild } from "@angular/core";
import { StoreService } from "../services/stores.service";
import { CookieService } from "ngx-cookie-service";

@Component({
  selector : 'stores',
  templateUrl : '../templates/stores.component.html',
  providers:[StoreService]
})
export class StoresComponent{
  constructor(private cookieService: CookieService) { }
  @Inject(StoreService) private service: StoreService
  image:any
  stores:any[]
  copy:any[]
  mymodel:any

  ngOnInit(): void {
    (async () => {
      const rawResponse = await fetch('http://localhost:3333/get_store/', {
        method: 'GET',
      })
      const content = await rawResponse.json();



      this.stores = content;
      this.copy = this.stores;
    })();
  }

  valuechange(newValue:any) {
    this.mymodel = newValue;
    console.log(newValue)
    this.stores =  this.copy.filter(store => store.name.toLowerCase().includes(newValue.toLowerCase()) )
  }
  trackstore(index:any,store:any){
    //this.image = 'data:image/jpg;base64,' + store.logo
  }

  addtoqueue(store:any){
    console.log(this.cookieService.get('userid'))
    console.log(store.id);
    this.cookieService.set('logo',store.logo);

    (async () => {
      const rawResponse = await fetch('http://localhost:3333/add_appointment/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          "user_id": this.cookieService.get('userid'),
          "store_id": store.id,
          "status" : "In_Queue"
        })
      })
      const content = await rawResponse.json();
      console.log(content)
      this.cookieService.set('storeid',content.store_id)

    })();

  }

}
