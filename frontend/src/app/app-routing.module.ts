import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from '../app/components/login.component';
import { CustomerDashboardComponent } from './components/customerdashboard.component';
import { StoresComponent } from './components/stores.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path : 'stores' , component: StoresComponent },
  { path : 'dashboard' , component : CustomerDashboardComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
