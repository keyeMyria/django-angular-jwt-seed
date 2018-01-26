import {Component} from '@angular/core';
import {Router} from '@angular/router';
import {FormGroup, FormControl, Validators} from '@angular/forms';
import {AuthenticationService} from '../authentication/index';

@Component({
  moduleId: module.id,
  selector: 'app-login',
  templateUrl: './login.component.html'
})
export class LoginComponent {
  errorHandler;
  form: FormGroup = new FormGroup({
    'username': new FormControl('', Validators.required),
    'password': new FormControl('', Validators.required),
  });

  constructor(private router: Router,
              private authService: AuthenticationService) {
  }

  public login() {
    this.authService
      .login(this.form.value)
      .subscribe(
        () => this.router.navigateByUrl('/'),
        error2 => {
          if (error2.status === 400) {
            this.onShowNotificationMessage('wrong username or password');
          }
        }
      );
  }

  private onShowNotificationMessage(msg) {
    this.errorHandler = msg;
    setTimeout(function () {
      this.errorHandler = null;
    }.bind(this), 2000);
  }
}
