import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginPageComponent } from './login-page/login-page.component';
import { AuthLayoutComponent } from './shared/layouts/auth-layout/auth-layout.component';
import { SiteLayoutComponent } from './shared/layouts/site-layout/site-layout.component';
import { RegisterPageComponent } from './register-page/register-page.component';
import { AuthGuard } from './shared/classes/auth.guard';
import { OverviewPageComponent } from './overview-page/overview-page.component';
import { CurrentPaymentsPageComponent } from './current-payments-page/current-payments-page.component';
import { ArchivePageComponent } from './archive-page/archive-page.component';
import { AnalyticsPageComponent } from './analytics-page/analytics-page.component';
import { CurrentPaymentsFormComponent } from './current-payments-page/current-payments-form/current-payments-form.component';

const routes: Routes = [
  {path:'', component:AuthLayoutComponent, children:[
    {path:'', redirectTo:'/login', pathMatch:'full'},
    {path:'login', component:LoginPageComponent},
    {path:'register', component:RegisterPageComponent}
  ]},
  {path:'', component:SiteLayoutComponent, canActivate:[AuthGuard], children:[
    {path:'overview', component:OverviewPageComponent},
    {path:'archive', component:ArchivePageComponent},
    {path:'analytics', component:AnalyticsPageComponent},
    {path:'currentpayments', component:CurrentPaymentsPageComponent},
    {path:'currentpayments/new', component:CurrentPaymentsFormComponent},
    {path:'currentpayments/:id', component:CurrentPaymentsFormComponent}
  ]}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
