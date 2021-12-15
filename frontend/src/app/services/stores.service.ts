import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class StoreService {
  constructor(private http: HttpClient) { }
  private url = "http://localhost:3333/"

  getstores(){
    (async () => {
      const rawResponse = await fetch('http://localhost:3333/get_store/', {
        method: 'GET',
      })
      const content = await rawResponse.json();

      console.log(content);
    })();
  }
}
