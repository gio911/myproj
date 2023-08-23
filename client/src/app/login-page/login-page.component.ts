import { Component, OnDestroy, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../shared/services/auth.services';
import { Subscription } from 'rxjs';
import { ActivatedRoute, Router } from '@angular/router';
import { MaterialService } from '../shared/classes/material.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent implements OnInit, OnDestroy {

  aSub!:Subscription;
  form!: FormGroup;

  constructor(private auth:AuthService, 
              private router:Router, 
              private route:ActivatedRoute,
              private toaster: ToastrService
              ){
    
  }
//Validators.email
//Validators.minLength(6)
  ngOnInit(): void {
    this.form=new FormGroup({
      username:new FormControl(null, [Validators.required]),
      password:new FormControl(null)
    })

    this.route.queryParams.subscribe((params)=>{
      if(params['registered']){
        this.toaster.success('Вы зарегистрировались в системе')
      }else if(params['accessDenide']){
        this.toaster.success('Для начала авторизуйтесь')
        MaterialService.toast('Для начала авторизуйтесь')
      }else if(params['tokenExpired']){
        this.toaster.success('Пожалуйста зайдите в систему заново')
      }
    })
  }

  ngOnDestroy(): void {
    if (this.aSub){
      this.aSub.unsubscribe()
    }
  }



  onSubmit(){
    this.form.disable()
    this.aSub = this.auth.login(this.form.value).subscribe({
      next:()=>this.router.navigate(['/overview']),
      error:(error)=>{
        MaterialService.toast(error.error.detail)
        console.warn(error);
        
        this.form.enable()
      }
      
  })
  }

}
