import {Component} from '@angular/core';
import {Router} from '@angular/router';
import {FormControl, FormGroup, Validators} from '@angular/forms';
import {AuthenticationService} from '../services/authentication.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html'
})
export class LoginComponent {
  errors;
  form: FormGroup = new FormGroup({
    'username': new FormControl('', Validators.required),
    'password': new FormControl('', Validators.required)
  });

  constructor(private router: Router,
              private _authService: AuthenticationService) {
  }
  public login() {
    this._authService
      .login(this.form.value)
      .subscribe(
        () => location.reload(true),
        e => {
          if (e.status === 400) {
            this.onShowNotificationMessage('wrong username or password');
          } else {
            this.onShowNotificationMessage(e.statusText);
          }
        }
      );
  }

  private onShowNotificationMessage(msg) {
    this.errors = msg;
    setTimeout(function() {
      this.errors = null;
    }.bind(this), 2000);
  }
}
