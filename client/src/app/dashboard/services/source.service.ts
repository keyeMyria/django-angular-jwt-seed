import {HttpClient} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {BehaviorSubject} from 'rxjs';
import {environment} from '../../../environments/environment';

import {ProfileModel} from '../models/profile.model';
import {MessagesService} from '../../shared/services';
import {filter, retry, tap} from 'rxjs/operators';


@Injectable()
export class SourceService {
  _baseUrl = environment.base_url;

  /** Stream that emits whenever the data has been modified. */
  private _data$ = <BehaviorSubject<ProfileModel>>new BehaviorSubject({});
  private _temp: ProfileModel;

  public data$ = this._data$.asObservable();

  set dataStream(value) {
    this._temp = value;
    this._data$.next(value);
  }

  constructor(private http: HttpClient, private _msgService: MessagesService) {
    this.loadQuerySet();
  }

  loadQuerySet() {
    const uri = `${this._baseUrl}profile/`;
    this.http.get<ProfileModel>(uri)
      .pipe(
        tap(debug => console.log('this.http.get', debug)),
        retry(5)
      )
      .subscribe(
        (data: ProfileModel) => this.dataStream = data,
        error => this._msgService.snack_notification$.next(error.message));
  }

}
